import logging

from flask import render_template, request, redirect
from src.main.service.task_service import TaskService

logger = logging.getLogger(__name__)

class TaskController:
    @staticmethod
    def get_tasks():
        tasks = TaskService.get_all_tasks()
        return render_template('index.html', tasks=tasks)

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
    def delete_task(cls, id):
        try:
            task = TaskService.delete_task(id)
            return redirect('/')
        except:
            return "there was problem deleting task"