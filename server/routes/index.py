from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()


class SearchString(BaseModel):
    string: str


@router.post("/")
def index(search_string: SearchString):
    return search_string.string
