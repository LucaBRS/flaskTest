# src/main/dao/task_dao.py
import logging

from sqlalchemy.orm import sessionmaker, Session

from main.model.person_model import Person
from main.model.task_model import TaskModule

logger = logging.getLogger(__name__)


class TaskDAO:

    def __init__(self, session: Session):
        self.session = session

    def get_all_tasks(self):
        logger.info("Retrieving all tasks")

        tasks = self.session.query(TaskModule).all()
        self.session.close()
        return tasks

    def post_task(self, task_content: str):
        logger.info(f"Posting task: {task_content}")

        new_task = TaskModule(content=task_content)
        self.session.add(new_task)
        self.session.commit()
        new_person = Person(name="1", surname="2", task_id=new_task.id)
        self.session.add(new_person)
        self.session.commit()
        self.session.close()

    def delete_task(self, id: int):
        logger.debug(f"Deleting task {id}")

        task_to_delete = self.session.query(TaskModule).get(id)
        self.session.delete(task_to_delete)
        self.session.commit()
        self.session.close()

    def get_task_by_id(self, id: int):
        task = self.session.query(TaskModule).get(id)
        self.session.close()
        return task

    def update_task_by_id(self, id: int, content: str):
        task_to_update = self.session.query(TaskModule).get(id)
        task_to_update.content = content
        self.session.commit()
        self.session.close()
