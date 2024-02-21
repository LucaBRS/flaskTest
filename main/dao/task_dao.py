# src/main/dao/task_dao.py
import logging


from main.model.person_model import Person
from main.model.task_model import Task
from main.config.sessions_configuration import sqlite_session


logger = logging.getLogger(__name__)


class TaskDAO:

    @classmethod
    def get_all_tasks(cls):
        session = sqlite_session
        logger.info("Retrieving all tasks")

        tasks = session.query(Task).all()
        session.close()
        return tasks

    @classmethod
    def post_task(cls, task_content: str):
        session = sqlite_session
        logger.info(f"Posting task: {task_content}")

        new_task = Task(content=task_content)
        session.add(new_task)
        session.commit()
        new_person = Person(name="1", surname="2", task_id=new_task.id)
        session.add(new_person)
        session.commit()
        session.close()

    @classmethod
    def delete_task(cls, id: int):
        session = sqlite_session
        logger.debug(f"Deleting task {id}")

        task_to_delete = session.query(Task).get(id)
        session.delete(task_to_delete)
        session.commit()
        session.close()

    @classmethod
    def get_task_by_id(cls, id: int):
        session = sqlite_session
        task = session.query(Task).get(id)
        session.close()
        return task

    @classmethod
    def update_task_by_id(cls, id: int, content: str):
        session = sqlite_session
        task_to_update = session.query(Task).get(id)
        task_to_update.content = content
        session.commit()
        session.close()
