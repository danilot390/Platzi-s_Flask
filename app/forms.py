from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Done')

class TaskForm(FlaskForm):
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Create')

class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Delete')

class UpdateTaskForm(FlaskForm):
    submit = SubmitField('Update')