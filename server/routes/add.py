from server.elastic import get_elastic, AsyncElasticsearch
from server.database import get_session, AsyncSession
from server.database.tables.document import Document
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import datetime
from json import dumps
router = APIRouter()


class DocumentModel(BaseModel):
    rubrics: list[str]
    text: str
    created_date: datetime


@router.post("/add")
async def add(new_document: DocumentModel, db_session: AsyncSession = Depends(get_session), elastic: AsyncElasticsearch = Depends(get_elastic)):
    new = Document(text=new_document.text, rubrics=dumps(new_document.rubrics), created_date=new_document.created_date)
    db_session.add(new)
    await db_session.commit()
    await elastic.create(index="document", document={
        "text": new_document.text
    }, id=str(new.id))
