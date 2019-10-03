from flask_wtf import FlaskForm
from wtforms import StringField, validators


class CommentForm(FlaskForm):
    comment_text = StringField("Kommentti", [validators.Length(min=4, max=50
    )])
   
    class Meta:
        csrf = False