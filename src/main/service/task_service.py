import logging

from sqlalchemy.orm import Session

from main.dao.task_dao import TaskDAO

logger = logging.getLogger(__name__)


class TaskService:
    def __init__(self, session: Session):
        self.task_dao = TaskDAO(session)

    def get_all_tasks(self):
        logger.info("Getting all tasks")
        return self.task_dao.get_all_tasks()

    def post_task(self, task_content: str):
        task_content = "$ " + task_content + " $"
        logger.info(f"Task content: {task_content}")
        return self.task_dao.post_task(task_content)

    def delete_task(self, id: int):
        logger.info(f"Deleting task {id}")
        return self.task_dao.delete_task(id)

    def get_task_by_id(self, id: int):
        return self.task_dao.get_task_by_id(id)

    def update_task_by_id(self, id: int, content: str):
        content = "$ " + content + " $"
        return self.task_dao.update_task_by_id(id, content)
