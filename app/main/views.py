from flask import render_template,redirect,url_for
from app import app

@app.route('/')
def index():
    '''
    view root page index page and its data
    '''
    title='GUIDE_PICK!'

    return render_template('index.html',title=title)