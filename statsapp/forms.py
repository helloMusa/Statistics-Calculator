from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import wtforms

class DataForm(FlaskForm):
	body = StringField('<h5>Enter Data: (seperated by commas)</h5>', validators=[DataRequired()])

class ArgForm(FlaskForm):
	body = StringField('<h5>Enter Data: (seperated by commas)</h5>', validators=[DataRequired()])
	arg = StringField('<h5>Enter Argument: </h5>', validators=[DataRequired()])
	submit = SubmitField(('Submit Data and Argument'))