from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField,PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo, Email
from flask_login import login_user,current_user
from models import db,Guide

from flask import Flask,render_template,flash,redirect,url_for
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt=Bcrypt(app)
Bootstrap(app)

app.config['SECRET_KEY']='2462d9f4cf69e22d4739a7ef'




class RegistrationForm (FlaskForm):
    Name= StringField('username', validators=[DataRequired(),Length(min=2, max=30)])
    email=StringField('email',validators=[DataRequired(),Email()])
    password=PasswordField('password',validators=[DataRequired(), Length(min=8, max=16)])
    confirm_password=PasswordField('confirm password',validators=[DataRequired(), Length(min=8, max=16), EqualTo('password')])
    languages= StringField('languages',validators=[DataRequired()])
    location=StringField('location',validators=[DataRequired()])
    submit=SubmitField('Sign up as A Guide')

class LoginForm(FlaskForm):
    email=StringField('email',validators=[DataRequired(), Email() ])
    password=PasswordField('password',validators=[DataRequired(), Length(min=8, max=16)])
    remember=BooleanField('Remember me')
    
    submit=SubmitField('Login ')   

class SearchForm(FlaskForm):
    search=StringField('search Guide by Location')
    submit=SubmitField('Submit')     

@app.route("/")
@app.route("/home")
def home():
    return  render_template("home.html")


@app.route("/register", methods=['GET','POST'] )
def register():
  form=RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    name= Guide(Name=form.Name.data, email=form.email.data, password= hashed_password, languages=form.languages.data, location=form.location.data )
    db.session.add(name)
    db.session.commit()
    flash(f'Account created You can Now Login!', 'success')
    return redirect(url_for('Login'))
  return  render_template("register.html", form=form)


@app.route("/Login")
def Login():
  form=LoginForm()
  return  render_template("Login.html",form=form)


@app.route("/search")
def search():
  form=SearchForm()
  return  render_template("search.html", form=form)


@app.route("/account")
def account():
    return  render_template("account.html")


@app.route("/display")
def display():
    return  render_template("display.html")

@app.route("/layout")
def layout():
    return  render_template("layout.html")


if __name__=='__main__':
  app.run(debug=True)