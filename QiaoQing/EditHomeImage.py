from flask_uploads import UploadSet, IMAGES
from wtforms import Form, BooleanField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired

photos = UploadSet('photos', IMAGES)

class EditHomeImageForm(Form):
    home_image = FileField(validators=[FileRequired()])
    home_policy = TextAreaField('Policy Description', validators=[DataRequired()])
    home_policy_image = FileField(validators=[FileRequired()])
