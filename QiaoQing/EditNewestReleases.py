from flask_uploads import UploadSet, IMAGES
from wtforms import Form, BooleanField, TextAreaField
#StringField, RadioField, SelectField, validators
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired

photos = UploadSet('photos', IMAGES)

class EditNewestReleasesForm(Form):
#    movie_title = TextAreaField('Movie Title', validators=[DataRequired()])
    release_image1 = FileField(validators=[FileRequired()])
    release_name1 = TextAreaField('New Release 1 Name', validators=[DataRequired()])
    release_image2 = FileField(validators=[FileRequired()])
    release_name2 = TextAreaField('New Release 2 Name', validators=[DataRequired()])
    release_image3 = FileField(validators=[FileRequired()])
    release_name3 = TextAreaField('New Release 3 Name', validators=[DataRequired()])
    release_image4 = FileField(validators=[FileRequired()])
    release_name4 = TextAreaField('New Release 4 Name', validators=[DataRequired()])
