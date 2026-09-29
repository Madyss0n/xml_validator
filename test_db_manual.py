from app.db import init_db, engine
from sqlalchemy import inspect

print("=== Тест: инициализация БД ===")
init_db()

inspector = inspect(engine)
tables = inspector.get_table_names()
print(f"Созданные таблицы: {tables}")

if "books" in tables:
    columns = inspector.get_columns("books")
    print("Структура таблицы 'books':")
    for col in columns:
        print(f"   {col['name']}: {col['type']}")
    print("✅ Таблица создана корректно")
else:
    print("❌ Таблица 'books' не найдена")