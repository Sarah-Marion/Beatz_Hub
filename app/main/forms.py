from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import Required, Email, Length, EqualTo, DataRequired
from app.models import Post, Comment, Subscribers
from flask_wtf.file import FileField, FileRequired, file_allowed

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(),Length(min=1, max=1000)])
    Entry= TextAreaField('Post your article', validators=[DataRequired(), Length(min=1, max=100000000000)])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Post Comment', [DataRequired(), Length(min=1)])
    commenter = StringField("Name" ,validators=[DataRequired()] )
    submit = SubmitField('Submit Comment')

def validate_subscriber(form, data_field):
    if Subscribers.query.filter_by(email= data_field.data).first():
        raise ValidationError('You are already subscribed')

class SubscribersForm(FlaskForm):
    email = StringField('Subscribe to get alerts', validators=[DataRequired(), Email(), Length(min=1, max=200), validate_subscriber])
    submit = SubmitField("Submit")