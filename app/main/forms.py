from flask_wtf import FlaskForm
from wtforms import StringField, FileField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo, Email

 



class UpdateAccountForm(FlaskForm):
  Name = StringField('name', validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  image_file = FileField('Update Profile Picture')
  languages = StringField('languages', validators=[DataRequired()])
  submit = SubmitField('Update')

class ReviewForm(FlaskForm):
  review=StringField('Leave a Review')
  submit=SubmitField('Submit')




  class SearchForm(FlaskForm):
    search=StringField('search Guide by Location')
    submit=SubmitField('Submit')
