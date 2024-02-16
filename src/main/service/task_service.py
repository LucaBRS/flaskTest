import logging

from sqlalchemy.orm import Session

from main.dao.task_dao import TaskDAO

logger = logging.getLogger(__name__)


class TaskService:

    @classmethod
    def get_all_tasks(self):
        logger.info("Getting all tasks")
        return TaskDAO.get_all_tasks()

    @classmethod
    def post_task(self, task_content: str):
        task_content = "$ " + task_content + " $"
        logger.info(f"Task content: {task_content}")
        return TaskDAO.post_task(task_content)

    @classmethod
    def delete_task(self, id: int):
        logger.info(f"Deleting task {id}")
        return TaskDAO.delete_task(id)

    @classmethod
    def get_task_by_id(self, id: int):
        return TaskDAO.get_task_by_id(id)

    @classmethod
    def update_task_by_id(self, id: int, content: str):
        content = "$ " + content + " $"
        return TaskDAO.update_task_by_id(id, content)
