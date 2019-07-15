from wtforms import StringField, TextAreaField, Form
from wtforms.validators import DataRequired


class PostForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Content', validators=[DataRequired()])
