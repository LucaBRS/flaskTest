import logging

from flask import render_template, request, redirect
from main.service.task_service import TaskService

logger = logging.getLogger(__name__)


class TaskController:
    def __init__(self,sessions:dict):
        self.task_service = TaskService(sessions['sqlite_session'])
    def get_tasks(self,gas_prices):
        tasks = self.task_service.get_all_tasks()
        return render_template('index.html', tasks=tasks, gas_prices=gas_prices)

    def post_task(self):
        task_content = request.form['task_content']
        logger.debug("Inserting task: %r" % task_content)

        try:
            self.task_service.post_task(task_content)
            return redirect('/')
        except Exception as e:
            logger.error("Error adding task: %s", e)
            return "There was an issue in adding the task"

    def delete_task(self, id: int):
        try:
            task = self.task_service.delete_task(id)
            return redirect('/')
        except:
            return "there was problem deleting task"

    def get_update_task(self, id: int):
        task = self.task_service.get_task_by_id(id)
        return render_template('update.html', task_to_update=task)

    def post_update_task(self, id: int):
        try:
            content = request.form['task_content_update']
            task = self.task_service.update_task_by_id(id, content)
            return redirect('/')
        except:
            return "there was problem updating task"
