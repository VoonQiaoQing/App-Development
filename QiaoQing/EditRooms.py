from flask_uploads import UploadSet, IMAGES
from wtforms import Form, TextAreaField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired

photos = UploadSet('photos', IMAGES)

class CreateRoomsForm(Form):
    room_title = TextAreaField('Rooms Pricings Title', validators=[DataRequired()])
    small_roominfo = TextAreaField('Small Room Information', validators=[DataRequired()])
    small_roomprice = IntegerField('Small Room Price',render_kw={"placeholder": "00"})
    small_roomimage1 = FileField(validators=[FileRequired()])
    small_roomimage2 = FileField(validators=[FileRequired()])
    med_roominfo = TextAreaField('Medium Room Information', validators=[DataRequired()])
    med_roomprice = IntegerField('Medium Room Price',render_kw={"placeholder": "00"})
    med_roomimage = FileField(validators=[FileRequired()])
    large_roominfo = TextAreaField('Large Room Information', validators=[DataRequired()])
    large_roomprice = IntegerField('Large Room Price',render_kw={"placeholder": "00"})
    large_roomimage1 = FileField(validators=[FileRequired()])
    large_roomimage2 = FileField(validators=[FileRequired()])

    gvexclusivesmall_roominfo =  TextAreaField('GV Exclusive Small Room Information', validators=[DataRequired()])
    gvexclusivesmall_roomprice = IntegerField('GV Exclusive Small Room Price',render_kw={"placeholder": "00"})
    gvexclusivemed_roominfo =  TextAreaField('GV Exclusive Medium Room Information', validators=[DataRequired()])
    gvexclusivemed_roomprice = IntegerField('GV Exclusive Medium Room Price',render_kw={"placeholder": "00"})
    gvexclusivelarge_roominfo = TextAreaField('GV Exclusive Large Room Information', validators=[DataRequired()])
    gvexclusivelargeroomprice =  IntegerField('GV Exclusive Large Room Price',render_kw={"placeholder": "00"})
