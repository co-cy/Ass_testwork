from server.elastic import get_elastic, AsyncElasticsearch
from server.database import get_session, AsyncSession
from server.database.tables.document import Document
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Iterator
from asyncio import gather
import json

router = APIRouter()


class SearchString(BaseModel):
    string: str


@router.post("/")
async def index(search_string: SearchString, db_session: AsyncSession = Depends(get_session),
                elastic: AsyncElasticsearch = Depends(get_elastic)):
    result = await elastic.search(index="document", query={"match": {"text": search_string.string}}, size=10)

    list_hits = list(map(lambda hit: int(hit["_id"]), result["hits"]["hits"]))
    list_doc = []
    for i in list_hits:
        list_doc.append(db_session.get(Document, i))

    doc_result: Iterator[Document] = sorted(await gather(*list_doc), key=lambda x: x.created_date, reverse=True)
    for doc in doc_result:
        doc.rubrics = json.loads(doc.rubrics)
    return doc_result
