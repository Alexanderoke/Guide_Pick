from flask import render_template,redirect,url_for
# from app.auth import forms
from app.main.forms import SearchForm
from app import app

@app.route("/")
def index():
    '''
    view root page index page and its data
    '''
    title='GUIDE_PICK!'
    form=SearchForm()

    return render_template("index.html",title=title, form=form)


@app.route("/register")
def register():
    
    return render_template("register.html",form=SearchForm)