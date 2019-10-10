from flask_wtf import FlaskForm
from wtforms import StringField, validators


class CommentForm(FlaskForm):
    comment_text = StringField("Kommentti", [validators.DataRequired()])
   
    class Meta:
        csrf = False