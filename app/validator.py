from lxml import etree
from pathlib import Path
from app.logger import setup_logger

logger = setup_logger(__name__)

SCHEMA_PATH = Path(__file__).parent / "schemas" / "books.xsd"

class XMLValidationError(Exception):
    """Кастомное исключение с человекочитаемым списком ошибок валидации."""
    def __init__(self, errors: list[str]):
        self.errors = errors
        super().__init__("; ".join(errors))


def _load_schema() -> etree.XMLSchema:
    logger.info(f"Загрузка XSD-схемы из: {SCHEMA_PATH.resolve()} (существует: {SCHEMA_PATH.exists()})")
# Врубаем если снова падает поиск схемы из schemas   logger.info(f"Содержимое папки schemas: {list(SCHEMA_PATH.parent.iterdir())}")
    try:
        with open(SCHEMA_PATH, "rb") as f:
            schema_doc = etree.parse(f)
        return etree.XMLSchema(schema_doc)
    except Exception as e:
        logger.exception("Не удалось загрузить XSD-схему")
        raise RuntimeError(f"Некорректная XSD-схема: {e}")


# Схему грузим один раз при импорте модуля, а не на каждый запрос
_schema = _load_schema()


def validate_xml(xml_bytes: bytes) -> etree.Element:
    """
    Парсит и валидирует XML-документ по схеме.
    Возвращает корневой элемент, если всё ок.
    Кидает XMLValidationError со списком причин, если нет.
    """
    try:
        tree = etree.fromstring(xml_bytes)
    except etree.XMLSyntaxError as e:
        logger.error(f"XML не является well-formed: {e}")
        raise XMLValidationError([f"Синтаксическая ошибка XML: {e}"])

    if not _schema.validate(tree):
        error_messages = [str(err) for err in _schema.error_log]
        logger.warning(f"Файл не прошёл валидацию по схеме: {error_messages}")
        raise XMLValidationError(error_messages)

    logger.info("XML успешно прошёл валидацию")
    return tree
