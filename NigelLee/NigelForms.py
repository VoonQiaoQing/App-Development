from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators

class CreateQuestionForm(Form):
    Question = StringField('Question', [validators.Length(min=1, max=150), validators.DataRequired()])
    Answer = StringField('Answer', [validators.Length(min=1, max=150), validators.DataRequired()])
    Availability = SelectField('Does the Chatbot have the answer?', [validators.DataRequired()], choices=[('', 'Select'), ('Yes', 'Yes'), ('No', 'No')], default='')
    NumberOfPeople= RadioField('Number of people who suggested this', choices=[('1', '1 to 10'), ('2', '11 to 20'), ('3', '21 to 30'),("4","Above 30 ")], default='1')
    remarks = TextAreaField('Remarks', [validators.Optional()])
