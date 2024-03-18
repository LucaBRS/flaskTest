import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger(__name__)


class DatabaseCreation:
    def __init__(self, db_path, tables):
        logger.debug("starting config for sqlite database")
        logger.info(db_path)
        engine = create_engine(db_path,pool_pre_ping=True)
        logger.debug(engine)

        #todo possible error under here if model are not well constructed
        for table in tables:
            logger.debug("setting up database with table: " + str(table))
            table.metadata.create_all(bind=engine)


        self.session_sqlite = sessionmaker(
            bind=engine)()  # the parenthesis is ESSENTIAL otherwise it wil not return SESSION

    def get_session(self):
        return self.session_sqlite
