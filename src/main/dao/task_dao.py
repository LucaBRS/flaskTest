# src/main/dao/task_dao.py
import logging

from src.main.model.sqlite_tables_models import TaskModule, db, Person

logger = logging.getLogger(__name__)


class TaskDAO:
    @staticmethod
    def get_all_tasks():
        logger.info("Retrieving all tasks")
        return TaskModule.query.order_by(TaskModule.date_created).all()

    @staticmethod
    def post_task(task_content: str):
        logger.info(f"Posting task: {task_content}")
        new_person = Person(name="1",surname="2", content=task_content)
        db.session.add(new_person)
        db.session.commit()
        new_task = TaskModule(content=task_content)
        db.session.add(new_task)
        db.session.commit()

    @classmethod
    def delete_task(cls, id: int):
        logger.debug(f"Deleting task {id}")
        task_to_delete = TaskModule.query.get_or_404(id)
        db.session.delete(task_to_delete)
        db.session.commit()

    @classmethod
    def get_task_by_id(cls, id: int):
        return TaskModule.query.get_or_404(id)

    @classmethod
    def update_task_by_id(cls, id: int, content: str):
        task_to_update = TaskModule.query.get_or_404(id)
        task_to_update.content = content
        db.session.commit()
        pass
