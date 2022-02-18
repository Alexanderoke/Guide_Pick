from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from app.models import Guide


class RegistrationForm(FlaskForm):
  Name = StringField('Name',validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email',validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  location = StringField('Location', validators=[DataRequired()])
  skill_set = StringField('skills', validators=[DataRequired()])
  languages = StringField('languages',validators=[DataRequired()])
  price = StringField('Price', validators=[DataRequired()])

  submit = SubmitField('Sign Up')


  def validate_email(self, email):
    user = Guide.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(), Email() ])
    password=PasswordField('password',validators=[DataRequired(), Length(min=8, max=16)])
    remember=BooleanField('Remember me')
    submit=SubmitField('Login ')