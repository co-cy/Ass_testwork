from server.elastic import get_elastic, AsyncElasticsearch
from server.database import get_session, AsyncSession
from server.database.tables.document import Document
from fastapi import APIRouter, Depends


router = APIRouter()


@router.delete("/delete")
async def delete(id: int, db_session: AsyncSession = Depends(get_session), elastic: AsyncElasticsearch = Depends(get_elastic)):
    document = await db_session.get(Document, id)
    if document:
        await db_session.delete(document)
        await db_session.commit()
        await elastic.delete(index="document", id=str(id))
        return "DELETED"
    else:
        return "NOT FOUND"

