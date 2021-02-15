from wtforms import Form, StringField, PasswordField, RadioField, SelectField, TextAreaField, validators, IntegerField
from wtforms import DateField
from wtforms.validators import InputRequired, Email


class Purchase(Form):
    Date = SelectField('',[validators.DataRequired()],choices =[] )
    Time = SelectField('',[validators.DataRequired()], choices=[])
    location = SelectField('',[validators.DataRequired()], choices=[])
    # roomtype = SelectField('',[validators.DataRequired()], choices=[('Small'), ('Medium'), ('Big')])
class Add_location(Form):
    location1 = StringField('Location 1', [validators.Length(min=1, max=150), validators.DataRequired()])
    location2 = StringField('Location 2', [validators.Length(min=1, max=150), validators.DataRequired()])
    location3 = StringField('Location 3')
    location4 = StringField('Location 4', [validators.Length(min=1, max=150), validators.DataRequired()])
    location5 = StringField('Location 5 ', [validators.Length(min=1, max=150), validators.DataRequired()])
class Add_time(Form):
    time1 = StringField('Time 1:', [validators.Length(min=1, max=150), validators.DataRequired()])
    time2 = StringField('Time 2:', [validators.Length(min=1, max=150), validators.DataRequired()])
    time3 = StringField('Time 3:', [validators.Length(min=1, max=150), validators.DataRequired()])
    time4 = StringField('Time 4:', [validators.Length(min=1, max=150), validators.DataRequired()])
    time5 = StringField('Time 5:', [validators.Length(min=1, max=150), validators.DataRequired()])
class Roomtype(Form):
    promocode = StringField('',render_kw={"placeholder": "e.g. Room2018"})
    roomtype = SelectField('',[validators.DataRequired()], choices=[('Small'), ('Medium'), ('Big')])
class Code(Form):
    small_code = StringField('',[validators.DataRequired()],render_kw={"placeholder": "Small Room Code"} )
    medium_code = StringField('',[validators.DataRequired()],render_kw={"placeholder": "Medium Room Code"})
    big_code = StringField('', [validators.DataRequired()],render_kw={"placeholder": "Big Room Code"})
    small_discount = IntegerField('',[validators.DataRequired()],render_kw={"placeholder": "eg.20, which is 20%"})
    medium_discount = IntegerField('',[ validators.DataRequired()],render_kw={"placeholder": "eg.20, which is 20%"})
    big_discount = IntegerField('',[ validators.DataRequired()],render_kw={"placeholder": "eg.20, which is 20%"})
class Date(Form):
    date1 = StringField('Date 1:',[validators.DataRequired()])
    date2 = StringField('Date 2:',[validators.DataRequired()])
    date3 = StringField('Date 3:',[validators.DataRequired()])
    date4 = StringField('Date 4:',[validators.DataRequired()])
    date5 = StringField('Date 5:',[validators.DataRequired()])

# class LoginForm(Form):
#
#     email = StringField("Email", validators=[validators.Length(min=7, max=50), validators.DataRequired(message="Please Fill This Field")])
#
#     password = PasswordField("Password", validators=[validators.DataRequired(message="Please Fill This Field")])
#
#
# class RegisterForm(Form):
#
#     username = StringField("Username", validators=[validators.Length(min=3, max=25), validators.DataRequired(message="Please Fill This Field")])
#
#     email = StringField("Email", [InputRequired("Please enter your email address."), Email("This field requires a valid email address")])
#
#     gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
#
#     password = PasswordField("Password", validators=[
#
#         validators.DataRequired(message="Please Fill This Field"),
#
#         validators.EqualTo(fieldname="confirm", message="Your Passwords Do Not Match")
#     ])
#
#     confirm = PasswordField("Confirm Password", validators=[validators.DataRequired(message="Please Fill This Field")])


# class CreateUserForm(Form):
#     Question = StringField('Question', [validators.Length(min=1, max=150), validators.DataRequired()])
#     Reason = StringField('Reason', [validators.Length(min=1, max=150), validators.DataRequired()])
#     Availability = SelectField('Does the Chatbot have the answer?', [validators.DataRequired()], choices=[('', 'Select'), ('Yes', 'Yes'), ('No', 'No')], default='')
#     NumberOfPeople= RadioField('Number of people who suggested this', choices=[('1', '1 to 10'), ('2', '11 to 20'), ('3', '21 to 30'),("4","Above 30 ")], default='1')
#     remarks = TextAreaField('Remarks', [validators.Optional()])

    # date6 = DateField('Date 6:', format= '%d-%m-%Y', render_kw={"placeholder": "DD-MM-YYYY"})
    # date7 = DateField('Date 7:', format= '%d-%m-%Y', render_kw={"placeholder": "DD-MM-YYYY"})

# class Admin_date(Form):
#     date = DateField('Date:', [validators.DataRequired()])

# class Availability(Form):
#     Date = SelectField('*Date:', [validators.DataRequired()], choices=[('', 'Select Date'), ('16th Jan 2021', '16th Jan 2021'), ('17th Jan 2021', '17th Jan 2021'), ('18th Jan 2021', '18th Jan 2021'),('19th Jan 2021', '19th Jan 2021'),('20th Jan 2021', '20th Jan 2021')], default='')
#     Time = SelectField('Time:',[validators.DataRequired()], choices=[('', 'Select Time'), ('9am', '9am'), ('12pm', '12pm'), ('3pm', '3pm'),('6pm', '6pm'),('9pm', '9pm')], default='')
#     AMKsmall = IntegerField()
#     AMKmedium = IntegerField()
#     AMKbig = IntegerField()
#     J8small = IntegerField()
#     J8medium = IntegerField()
#     J8big = IntegerField()
#     CYCCsmall = IntegerField()
#     CYCCmedium = IntegerField()
#     CYCCbig = IntegerField()
#     BPsmall = IntegerField()
#     BPmedium = IntegerField()
#     BPbig = IntegerField()
#     JCubesmall = IntegerField()
#     JCubemedium = IntegerField()
#     JCubebig = IntegerField()
#     OTHsmall = IntegerField()
#     OTHmedium = IntegerField()
#     OTHbig = IntegerField()


    # date1 = DateField('Date 1:', format= '%Y-%m-%d', render_kw={"placeholder": "YYYY-MM-DD"})
    # date2 = DateField('Date 2:', format= '%Y-%m-%d', render_kw={"placeholder": "YYYY-MM-DD"})
    # date3 =
#Form object – Used to create a WTForms Form.
#StringField object – Used to create an HTML textfield.
#RadioField object – Used to create an HTML radio button group.
#SelectField object – Used to create an HTML dropdown list.
#TextAreaField object – Used to create an HTML textarea.
#validators object – validators allow you to specify the constraints for each of the fields such as minimum and maximum length, DataRequried or Optional.
 # expiry_month = DateField('Expiry Month:', format= '%m', render_kw={"placeholder": "00"})
