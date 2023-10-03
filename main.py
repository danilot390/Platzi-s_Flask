from flask import request, make_response, redirect, render_template, session, url_for, flash

import unittest

from app import create_app

app = create_app()

todos = ['Make  coffe', 'Sent message', 'Deliver Video ']


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

@app.route('/hello', methods=['GET'])
def hello():
    user_ip = session.get("user_ip")
    user = session.get('user')
    context = {
        'user_ip' : user_ip,
        'todos'   : todos,
        'user' : user,
    }

    return render_template('hello.html', **context)
