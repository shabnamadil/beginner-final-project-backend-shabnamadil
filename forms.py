from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User

class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(max=20)])
    email = StringField('email', validators=[DataRequired(), Email(), Length(max=30)])
    subject = StringField('subject', validators=[DataRequired()])
    message = TextAreaField('message', validators=[DataRequired(), Length(max=255)])


class NewsLetterForm(FlaskForm):
    
    name = StringField('name', validators=[DataRequired(), Length(max=20)])
    email = StringField('email', validators=[DataRequired(), Email(), Length(max=30)])


class RegisterForm(FlaskForm):
    def validate_email(form,field):
      if User.query.filter_by(email=field.data).count()>0:
        raise ValidationError('You have registered before')
      
    full_name = StringField('full_name', validators=[DataRequired(), Length(max=20, min=5)])
    email = StringField('email', validators=[DataRequired(), Email(), Length(max=30)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=30)])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), Length(min=8, max=30), EqualTo('password') ])


class LoginForm(FlaskForm):
    def validate_email(form,field):
      if User.query.filter_by(email=field.data).count()<0:
         raise ValidationError('You need to register')
    email = StringField('email', validators=[DataRequired(), Email(), Length(max=30)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8, max=30)])

class FavoriteForm(FlaskForm):
    submit = SubmitField('submit')
    size = BooleanField('size')

class RemoveForm(FlaskForm):
    submit = SubmitField('submit')

class SearchForm(FlaskForm):
    searchword = StringField('search', validators=[DataRequired()])
    submit = SubmitField('submit')

class ReviewForm(FlaskForm):
    review = TextAreaField('review', validators=[DataRequired(), Length(max=250)])
  

