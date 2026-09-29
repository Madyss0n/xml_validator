from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publish_date = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Book(name={self.name!r}, author={self.author!r}, publish_date={self.publish_date})>"