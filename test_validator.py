from app.validator import validate_xml, XMLValidationError

# === Кейс 1: корректный XML ===
good_xml = """<?xml version="1.0" encoding="UTF-8"?>
<Books xmlns="http://mephi3.ru">
    <book>
        <name>Война и мир</name>
        <author>Толстой</author>
        <publishDate>1869-01-01</publishDate>
    </book>
</Books>""".encode("utf-8")

print("=== Тест 1: корректный XML ===")
try:
    validate_xml(good_xml)
    print("✅ Валидация пройдена (ожидаемо)")
except XMLValidationError as e:
    print("❌ Ошибки (не ожидалось!):", e.errors)

print()

# === Кейс 2: отсутствует обязательное поле author ===
bad_xml_missing_field = """<?xml version="1.0" encoding="UTF-8"?>
<Books xmlns="http://mephi3.ru">
    <book>
        <name>Тестовая книга</name>
        <publishDate>2020-01-01</publishDate>
    </book>
</Books>""".encode("utf-8")

print("=== Тест 2: отсутствует поле author ===")
try:
    validate_xml(bad_xml_missing_field)
    print("✅ Валидация пройдена (не должно было!)")
except XMLValidationError as e:
    print("❌ Ошибки (ожидаемо):", e.errors)

print()

# === Кейс 3: битый (не well-formed) XML — незакрытый тег ===
bad_xml_syntax = """<?xml version="1.0" encoding="UTF-8"?>
<Books xmlns="http://mephi3.ru">
    <book>
        <name>Без закрытия
    </book>
</Books>""".encode("utf-8")

print("=== Тест 3: синтаксически некорректный XML ===")
try:
    validate_xml(bad_xml_syntax)
    print("✅ Валидация пройдена (не должно было!)")
except XMLValidationError as e:
    print("❌ Ошибки (ожидаемо):", e.errors)