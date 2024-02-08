import logging

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

logging.basicConfig(level=logging.DEBUG)
logger = app.logger
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    #this is going to be set automatically!
    date_created = db.Column(db.DateTime, default=datetime.utcnow())


    def __repr__(self):
        return "<Task %r>" % self.id

@app.route('/', methods=['GET','POST'])
def hello_world():  # put application's code here
    if request.method == 'POST':
        #request of the form created they have to have same name....
        task_content = request.form['task_content']
        logger.debug("inserting task %r" % task_content)
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "there was issue in adding task"
    else:
         tasks = Todo.query.order_by(Todo.date_created).all()
         return render_template('index.html',tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        logger.debug('trying to delete task: ' + str(task_to_delete))
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "there was problem deleting task"

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task_to_update.content = request.form['task_content_update']

        try:
            #we just have to commit because we already sert the content before
            db.session.commit()
            return redirect('/')
        except:
            return "there was an issue in updating task"
    else:
        return render_template('update.html',task_to_update=task_to_update)

if __name__ == '__main__':
    app.run(debug=True)
