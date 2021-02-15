from wtforms import Form, StringField , validators, IntegerField, DateField

class Checkout(Form):
    card_number1= IntegerField('',render_kw={"placeholder": "1234 1234 1234 1234"})
    # card_number2= IntegerField('',render_kw={"placeholder": "0000"})
    # card_number3= IntegerField('',render_kw={"placeholder": "0000"})
    # card_number4= IntegerField('',render_kw={"placeholder": "0000"})
    name_on_card = StringField('', [validators.length(min=1, max=50), validators.DataRequired()],render_kw={"placeholder": "Name"})
    expiry_month = DateField('', format= '%m', render_kw={"placeholder": "MM"})
    expiry_year = DateField('', format= '%Y', render_kw={"placeholder": "YYYY"})
    cvv_number = IntegerField('',render_kw={"placeholder": "000"})

    #promocode = StringField('Promo Code:', [validators.length(min=1, max=100)], render_kw={"placeholder": "Promo Code"})

    #  card_number= IntegerField('Card Number:', [validators.number_range(min=16, max=16), validators.DataRequired()],render_kw={"placeholder": "0000-0000-0000-0000"})
    # name_on_card = StringField('Name On Card:', [validators.length(min=1, max=50), validators.DataRequired()],render_kw={"placeholder": "Name"})
    # expiry_month = DateField('Expiry Month:', format= '%m', render_kw={"placeholder": "00"})
    # expiry_year = IntegerField('Expiry Year:', [validators.number_range(min=4, max=4), validators.DataRequired()],render_kw={"placeholder": "0000"})
    # cvv_number = IntegerField('CVV Number:', [validators.number_range(min=3, max=3), validators.DataRequired()],render_kw={"placeholder": "000"})
    # promocode = StringField('Promo Code:', [validators.length(min=1, max=100)], render_kw={"placeholder": "Promo Code"})
