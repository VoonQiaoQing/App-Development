from wtforms import Form, SelectField, TextAreaField, validators


class CreateUserForm(Form):
    rating = SelectField('Rating', [validators.DataRequired()], choices=[('', 'Select'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='')
    review = TextAreaField('Review', [validators.length(min=1)])
