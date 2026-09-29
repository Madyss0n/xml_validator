from app.validator import validate_xml
from app.repository import parse_books_from_xml, save_books
from app.db import init_db, SessionLocal

xml_data = """<?xml version="1.0" encoding="UTF-8"?>
<Books xmlns="http://mephi3.ru">
    <book>
        <name>Война и мир</name>
        <author>Толстой</author>
        <publishDate>1869-01-01</publishDate>
    </book>
    <book>
        <name>Преступление и наказание</name>
        <author>Достоевский</author>
        <publishDate>1866-01-01</publishDate>
    </book>
</Books>""".encode("utf-8")

init_db()

tree = validate_xml(xml_data)
books = parse_books_from_xml(tree)

session = SessionLocal()
save_books(session, books)

# Проверка, что реально записалось
from app.models import Book
all_books = session.query(Book).all()
print(f"Всего книг в БД: {len(all_books)}")
for b in all_books:
    print(f"  {b}")

session.close()