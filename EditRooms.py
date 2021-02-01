from flask_uploads import UploadSet, IMAGES
from wtforms import Form, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired

photos = UploadSet('photos', IMAGES)

class CreateRoomsForm(Form):
    room_title = TextAreaField('Rooms Pricings Title', validators=[DataRequired()])
    small_roominfo = TextAreaField('Small Room Information', validators=[DataRequired()])
    small_roomimage1 = FileField(validators=[FileRequired()])
    small_roomimage2 = FileField(validators=[FileRequired()])
    med_roominfo = TextAreaField('Medium Room Information', validators=[DataRequired()])
    med_roomimage = FileField(validators=[FileRequired()])
    large_roominfo = TextAreaField('Large Room Information', validators=[DataRequired()])
    large_roomimage1 = FileField(validators=[FileRequired()])
    large_roomimage2 = FileField(validators=[FileRequired()])
    gvexclusiveinfo =  TextAreaField('GV Exclusive Information', validators=[DataRequired()])

