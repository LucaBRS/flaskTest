import logging

from src.main.dao.task_dao import TaskDAO
logger = logging.getLogger(__name__)

class TaskService:
    @staticmethod
    def get_all_tasks():
        logger.info("Getting all tasks")
        return TaskDAO.get_all_tasks()

    @staticmethod
    def post_task( task_content):
        logger.info(f"Task content: {task_content}")
        return TaskDAO.post_task(task_content)

    @classmethod
    def delete_task(cls, id):
        logger.info(f"Deleting task {id}")
        return TaskDAO.delete_task(id)
