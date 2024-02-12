# src/main/dao/task_dao.py
import logging

from main.model.sqlite_tables_models import TaskModule, Person, Session_sqlite

logger = logging.getLogger(__name__)




class TaskDAO:
    @staticmethod
    def get_all_tasks():
        logger.info("Retrieving all tasks")
        session = Session_sqlite()
        tasks = session.query(TaskModule).all()
        session.close()
        return tasks


    @staticmethod


    def post_task(task_content: str):
        logger.info(f"Posting task: {task_content}")
        session = Session_sqlite()
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
        session = Session_sqlite()
        task_to_delete = session.query(TaskModule).get(id)
        session.delete(task_to_delete)
        session.commit()
        session.close()


    @classmethod
    def get_task_by_id(cls, id: int):
        session = Session_sqlite()
        task = session.query(TaskModule).get(id)
        session.close()
        return task

    @classmethod
    def update_task_by_id(cls, id: int, content: str):
        session = Session_sqlite()
        task_to_update = session.query(TaskModule).get(id)
        task_to_update.content = content
        session.commit()
        session.close()

