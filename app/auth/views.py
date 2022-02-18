from flask import render_template
from app import app

@app.route('/auth')
def index() :
  return render_template('register.html')