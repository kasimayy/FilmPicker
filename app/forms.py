from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from app.models import Film

class AddFilmForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	year = IntegerField('Year', validators=[DataRequired()])
	genre = StringField('Genres')
	platform = StringField('Available on')
	summary = StringField('Summary', validators=[DataRequired()])
	image_url = StringField('Image URL')
	submit = SubmitField('Add Film')