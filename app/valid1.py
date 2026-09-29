from app.logger import setup_logger
logger = setup_logger(__name__)

logger.info("Проходит валидация файла")
logger.error(f"Ошибка валидации файла: ")
