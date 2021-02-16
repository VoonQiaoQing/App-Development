from wtforms import Form, StringField, PasswordField, SelectField, RadioField, TextAreaField, validators
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed


class LoginForm(Form):

    email = StringField("Email", validators=[validators.Length(min=7, max=50), validators.DataRequired(message="Please Fill This Field")])

    password = PasswordField("Password", validators=[validators.DataRequired(message="Please Fill This Field")])


class RegisterForm(Form):

    username = StringField("Username", validators=[validators.Length(min=3, max=25), validators.DataRequired(message="Please Fill This Field")])

    email = StringField("Email", [InputRequired("Please enter your email address."), Email("This field requires a valid email address")])

    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')

    password = PasswordField("Password", validators=[

        validators.DataRequired(message="Please Fill This Field"),

        validators.EqualTo(fieldname="confirm", message="Your Passwords Do Not Match")
    ])

    confirm = PasswordField("Confirm Password", validators=[validators.DataRequired(message="Please Fill This Field")])

    profile = FileField('Profile', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif'], 'Images only!')])


class CreateUserForm(Form):
    Question = StringField('Question', [validators.Length(min=1, max=150), validators.DataRequired()])
    Reason = StringField('Reason', [validators.Length(min=1, max=150), validators.DataRequired()])
    Availability = SelectField('Does the Chatbot have the answer?', [validators.DataRequired()], choices=[('', 'Select'), ('Yes', 'Yes'), ('No', 'No')], default='')
    NumberOfPeople= RadioField('Number of people who suggested this', choices=[('1', '1 to 10'), ('2', '11 to 20'), ('3', '21 to 30'),("4","Above 30 ")], default='1')
    remarks = TextAreaField('Remarks', [validators.Optional()])
