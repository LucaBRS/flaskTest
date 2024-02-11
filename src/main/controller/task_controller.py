import logging

from flask import render_template, request, redirect
from src.main.service.task_service import TaskService

logger = logging.getLogger(__name__)


class TaskController:
    @staticmethod
    def get_tasks(gas_prices):
        tasks = TaskService.get_all_tasks()
        return render_template('index.html', tasks=tasks, gas_prices=gas_prices)

    @classmethod
    def post_task(cls):
        task_content = request.form['task_content']
        logger.debug("Inserting task: %r" % task_content)

        try:
            TaskService.post_task(task_content)
            return redirect('/')
        except Exception as e:
            logger.error("Error adding task: %s", e)
            return "There was an issue in adding the task"

    @classmethod
    def delete_task(cls, id: int):
        try:
            task = TaskService.delete_task(id)
            return redirect('/')
        except:
            return "there was problem deleting task"

    @classmethod
    def get_update_task(cls, id: int):
        task = TaskService.get_task_by_id(id)
        return render_template('update.html', task_to_update=task)

    @classmethod
    def post_update_task(cls, id: int):
        try:
            content = request.form['task_content_update']
            task = TaskService.update_task_by_id(id, content)
            return redirect('/')
        except:
            return "there was problem updating task"
