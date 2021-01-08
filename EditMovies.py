from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators

class CreateMoviesForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])

#Form object – Used to create a WTForms Form.
#StringField object – Used to create an HTML textfield.
#RadioField object – Used to create an HTML radio button group.
#SelectField object – Used to create an HTML dropdown list.
#TextAreaField object – Used to create an HTML textarea.
#validators object – validators allow you to specify the constraints for each of the fields such as minimum and maximum length, DataRequried or Optional.
