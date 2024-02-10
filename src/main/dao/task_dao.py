# src/main/dao/task_dao.py
import logging

from src.main.model.task_model import TaskModule, db
logger = logging.getLogger(__name__)


class TaskDAO:
    @staticmethod
    def get_all_tasks():
        logger.info("Retrieving all tasks")
        return TaskModule.query.order_by(TaskModule.date_created).all()

    @staticmethod
    def post_task(task_content):
        logger.info(f"Posting task: {task_content}")
        new_task = TaskModule(content=task_content)
        db.session.add(new_task)
        db.session.commit()

    @classmethod
    def delete_task(cls, id):
        logger.debug(f"Deleting task {id}")
        task_to_delete = TaskModule.query.get_or_404(id)
        db.session.delete(task_to_delete)
        db.session.commit()
