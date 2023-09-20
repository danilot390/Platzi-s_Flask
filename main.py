from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'This way'


todos = ['Make  coffe', 'Sent message', 'Deliver Video ']


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sent')


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
    login_form = LoginForm()
    user = session.get('user')
    context = {
        'login_form' : login_form,
        'user_ip' : user_ip,
        'todos'   : todos,
        'user' : user,
    }

    return render_template('hello.html', **context)

@app.route('/hello', methods=['POST'])
def hello_post():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = login_form.username.data
        session['user'] = user
        context = {
            'login_form' : login_form,
            'todos'   : todos,
            'user' : user,
        }

        return render_template('hello.html', **context)

    return render_template('hello.html')