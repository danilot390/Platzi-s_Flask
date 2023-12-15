from flask import redirect, url_for, render_template, render_template, session, flash
from flask_bootstrap import Bootstrap
from flask_login import login_user, login_required, logout_user

from app.forms import LoginForm
from werkzeug.security import generate_password_hash

from . import auth
from app.firestore_service import get_user, create_user
from app.models import UserData, UserModel

@auth.route('/login', methods = ['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form,
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user_doc = get_user(username)
        if user_doc is not None:
            password_from_db = user_doc['password']

            if password == password_from_db:
                user_data = UserData(user_doc['id'],username, password)
                user = UserModel(user_data)

                login_user(user)

                flash('Welcome again ;)')
                
                return redirect(url_for('hello'))
            else:
                flash("The passsword doesn't match...")
        else:
            flash("User doesn't exist!...")
    return render_template('login.html', **context)

@auth.route('signup', methods = ['GET', 'POST'])
def signup():
    signup_form = LoginForm()
    context = {
        'signup_form': signup_form,
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        user_doc = get_user(username)

        if user_doc is None:
            password = generate_password_hash(password)
            user_data = UserData(id=2,username=username, password=password)

            create_user(user_data)

            user = UserModel(user_data)

            login_user(user)

            flash('Welcome')

            return redirect(url_for('hello'))
        else:
            flash('The user Exist')

    return render_template('signup.html', **context)

@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('Have a good one!!!')

    return redirect(url_for('auth.login'))