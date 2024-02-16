import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


logger = logging.getLogger(__name__)


class DatabaseCreation():
    def __init__(self, db_path,tables):
        logger.debug("starting config for sqlite database")
        engine = create_engine(db_path)
        for table in tables:
            table.metadata.create_all(bind=engine)
        self.session_sqlite = sessionmaker(
            bind=engine)()  # the parenthesis is ESSENTIAL otherwise it wil not return SESSION

    def get_session(self):
        return self.session_sqlite
