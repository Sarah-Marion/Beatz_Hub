from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import Required, Email, Length, EqualTo, DataRequired
from app.models import Post, Comment, Subscribers
from flask_wtf.file import FileField, FileRequired, file_allowed

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()],  render_kw={"placeholder": "title"})
    Entry= TextAreaField('Post your article', validators=[DataRequired()], render_kw={"placeholder": "Post article"})
    youtube = StringField('Youtube Video',  render_kw={"placeholder": "YouTube link"})
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Post Comment', [DataRequired(), Length(min=1)],  render_kw={"placeholder": "Comment"})
    commenter = StringField("Name" ,validators=[DataRequired()],  render_kw={"placeholder": "Name"})
    submit = SubmitField('Submit Comment')

def validate_subscriber(form, data_field):
    if Subscribers.query.filter_by(email= data_field.data).first():
        raise ValidationError('You are already subscribed')

class SubscribersForm(FlaskForm):
    email = StringField('Subscribe to get alerts', validators=[DataRequired(), Email(), Length(min=1, max=200), validate_subscriber])
    submit = SubmitField("Submit")