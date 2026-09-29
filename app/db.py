from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from app.logger import setup_logger

logger = setup_logger(__name__)

DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def init_db():
    """Создаёт таблицы, если их ещё нет."""
    logger.info(f"Инициализация БД: {DATABASE_URL}")
    Base.metadata.create_all(bind=engine)