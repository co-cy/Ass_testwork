from sqlalchemy import Column, Text, Integer, DateTime
from server.database import Base


class Document(Base):
    __tablename__ = "document"

    id = Column(Integer, primary_key=True)
    # TODO Перенести в отдельную таблицу с рубриками (чтобы можно было с ними что-то делать)
    rubrics = Column(Text)
    text = Column(Text)
    created_date = Column(DateTime, index=True)
