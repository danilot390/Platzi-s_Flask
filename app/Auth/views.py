from flask import render_template, render_template, session, flash
from flask_bootstrap import Bootstrap


from app.forms import LoginForm


from . import auth

@auth.route('/login')
def login():
    context = {
        'login_form': LoginForm(),
    }
    return render_template('login.html', **context)

@auth.route('/login', methods=['POST'])
def login_post():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = login_form.username.data
        session['user'] = user

        flash('User successfully!!')
        context = {
            'user' : user,
        }

        return render_template('hello.html', **context)

    return render_template('login.html')