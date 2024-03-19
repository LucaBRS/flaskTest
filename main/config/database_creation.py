import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

logger = logging.getLogger(__name__)


class DatabaseCreation:
    def __init__(self, db_path, tables, Base: declarative_base):
        logger.debug("starting config for sqlite database")
        logger.info(db_path)
        engine = create_engine(db_path, pool_pre_ping=True)
        logger.debug(engine)

        # todo possible error under here if model are not well constructed
        # for table in tables:
        #     logger.debug("setting up database with table: " + str(table))
        #     table.metadata.create_all(bind=engine)

        self.db_session = scoped_session(sessionmaker(bind=engine))  # scoped_session is useful for multi tread like web app (manages the lifecycle of sessions within the context of a thread)
        Base.query = self.db_session.query_property()
        Base.metadata.create_all(bind=engine)

    def get_session(self):
        return self.db_session
