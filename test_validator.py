from app.validator import validate_xml, XMLValidationError

good_xml = """<?xml version="1.0" encoding="UTF-8"?>
<Books xmlns="http://mephi3.ru">
    <book>
        <name>Война и мир</name>
        <author>Толстой</author>
        <publishDate>1869-01-01</publishDate>
    </book>
</Books>""".encode("utf-8")

try:
    validate_xml(good_xml)
    print("✅ Валидация пройдена")
except XMLValidationError as e:
    print("❌ Ошибки:", e.errors)
