# src/main/dao/task_dao.py
import logging

from sqlalchemy.orm import sessionmaker

from main.model.person_model import Person
from main.model.task_model import TaskModule
from main.config.sqllite_config import Session_sqlite,Session_sqlite_test

logger = logging.getLogger(__name__)




class TaskDAO:

    session = Session_sqlite()

    @classmethod
    def get_all_tasks(cls):
        logger.info("Retrieving all tasks")
        session = cls.session
        tasks = session.query(TaskModule).all()
        session.close()
        return tasks

    @classmethod
    def post_task(cls,task_content: str):
        logger.info(f"Posting task: {task_content}")
        session = cls.session
        new_task = TaskModule(content=task_content)
        session.add(new_task)
        session.commit()
        new_person = Person(name="1", surname="2", task_id=new_task.id)
        session.add(new_person)
        session.commit()
        session.close()

    @classmethod
    def delete_task(cls, id: int):
        logger.debug(f"Deleting task {id}")
        session = cls.session
        task_to_delete = session.query(TaskModule).get(id)
        session.delete(task_to_delete)
        session.commit()
        session.close()

    @classmethod
    def get_task_by_id(cls, id: int):
        session = cls.session
        task = session.query(TaskModule).get(id)
        session.close()
        return task

    @classmethod
    def update_task_by_id(cls, id: int, content: str):
        session = cls.session
        task_to_update = session.query(TaskModule).get(id)
        task_to_update.content = content
        session.commit()
        session.close()

    @classmethod
    def __test_session_change__(cls):
        cls.session = Session_sqlite_test()

