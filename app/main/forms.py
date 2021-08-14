from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required
from ..models import Categories




class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

# def cats():
#     return Categories.query

class PitchForm(FlaskForm):
    title = StringField('Enter the title of your pitch pitch',validators=[Required()])
    pitch = StringField('Enter your pitch',validators=[Required()])
    # category = SelectField('Select Category', query_factory=cats)
    submit = SubmitField('Post')


    # hour = SelectField(u'Hour', choices=HOUR_CHOICES)