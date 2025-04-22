from typing import Any
import sys
from typing import Generator

from sqlmodel import Session, SQLModel, create_engine

from .config import config

try:
    from logging_config import logger
except ImportError:
    from .logging_config import logger


DATABASE_URL: str = config.DATABASE_URL


if not DATABASE_URL:
    logger.error('No DATABASE_URL found in .env file. Exiting...')
    sys.exit(1)

try:
    logger.debug('Connecting to the database')
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        connection.close()
    logger.debug('Successfully connected to the database')
except Exception as e:
    logger.error(f'Failed to connect to the database: {e}')
    sys.exit(1)


def add_db_metadata():
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, Any, None]:
    with Session(engine) as session:
        yield session
