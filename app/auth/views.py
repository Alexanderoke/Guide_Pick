from flask import render_template,url_for,flash,redirect
from app.auth import app, db, bcrypt
from app.auth.forms import RegistrationForm,LoginForm
from models import Guide

@app.route("/register", methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user= Guide(Name=form.Name.data, email=form.Email.data, password= hashed_password )
    db.session.add(user)
    db.session.commit()
    flash(f'Account created You can Now Login!', 'success')
    return redirect(url_for('Login'))
  return render_template('auth/register.html',title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('auth/login.html', title='Login', form=form)