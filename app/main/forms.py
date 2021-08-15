from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SelectField,SubmitField
from wtforms.validators import Required
from wtforms.ext.sqlalchemy.fields import QuerySelectField




class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')



class PitchForm(FlaskForm):
    title = StringField('Enter the title of your pitch',validators=[Required()])
    pitch = TextAreaField('Enter your pitch',validators=[Required()])
    category =SelectField("Pitch category",choices=[('Product Pitch','Product Pitch'),('Interview Pitch','Interview Pitch'), ('Technology Pitch','Technology Pitch'), ('Fashion Pitch','Fashion Pitch')],validators=[Required()])    
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Add a comment', validators=[Required()])
    submit = SubmitField('Post')
