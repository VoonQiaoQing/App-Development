from wtforms import Form, TextAreaField
from wtforms.validators import DataRequired

class EditHomeDescriptionForm(Form):
    home_description = TextAreaField('Home Description', validators=[DataRequired()])
