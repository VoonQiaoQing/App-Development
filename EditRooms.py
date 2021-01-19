from wtforms import Form, FileField, RadioField, SelectField, TextAreaField, validators

class CreateRoomsForm(Form):
    room_title = TextAreaField('Rooms Pricings Title', [validators.DataRequired()])
    small_roominfo = TextAreaField('Small Room Information', [validators.DataRequired()])
#    small_roomimage =
    med_roominfo = TextAreaField('Medium Room Information', [validators.DataRequired()])
#    med_roomimage1 =
#    med_roomimage2 =
    large_roominfo = TextAreaField('Large Room Information', [validators.DataRequired()])
#    large_roomimage1 =
#    large_roomimage2 =
    gvexclusiveinfo =  TextAreaField('GV Exclusive Information', [validators.DataRequired()])
#Form object – Used to create a WTForms Form.
#StringField object – Used to create an HTML textfield.
#RadioField object – Used to create an HTML radio button group.
#SelectField object – Used to create an HTML dropdown list.
#TextAreaField object – Used to create an HTML textarea.
#validators object – validators allow you to specify the constraints for each of the fields such as minimum and maximum length, DataRequried or Optional.

