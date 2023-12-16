from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_login import login_required, current_user, LoginManager
import unittest

from app import create_app
from app.firestore_service import get_user, get_tasks, create_task, delete_task
from app.forms import TaskForm, DeleteTaskForm
app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

    #need: export FLASK_APP=main.py

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    user_ip = session.get("user_ip")
    user = current_user
    task_form = TaskForm()
    delete_task_form = DeleteTaskForm()
    
    if task_form.validate_on_submit():

        create_task(user_id=str(user.id), description=task_form.description.data)
        flash('A new task has been created')
        
        return redirect(url_for('hello'))

    tasks = get_tasks(str(user.id))

    context = {
        'user_ip' : user_ip,
        'tasks'   : tasks,
        'user' : user,
        'task_form' : task_form,
        'delete_form' : delete_task_form
    }
    
    return render_template('hello.html', **context)

@app.route('/task/delete/<task_id>', methods=['POST'])
def delete_tasks(task_id):
    user_id = current_user.id
    delete_task(user_id, task_id)

    return redirect(url_for('hello'))