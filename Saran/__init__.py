import shelve, payment, booking,random,string
from flask import Flask, render_template, request, redirect, url_for, session
from EditMovies import CreateMoviesForm
from Forms import Purchase, Add_time, Add_location, Roomtype, Code
from checkoutform import Checkout
import rooms as rooms
import roomLoactionCapacity as room
import movieinfo as movieinfo
import admin as admin
from pathlib import Path
app = Flask(__name__)

@app.route('/')
def home():
    available_dict = {}
    db = shelve.open('storage.db','c')
    try:
        available_dict = db['Available']
    except:
        print('Error in retrieving form from admin_location.db')
    available = booking.Left(5,5,5)
    DTL = booking.Booking('20Jan','9am','Bishan')
    available_dict[DTL] = available
    db['Available'] = available_dict
    db.close()
    return render_template('home.html')
@app.route('/Movies')
def movies():
    return render_template('movies.html')

@app.route('/filter')
def vmd_timestamp():
    return render_template('moviesfilter.html')
# Location
@app.route('/add_location', methods=['GET', 'POST'])
def add_location():
    add_location_form = Add_location(request.form)
    if request.method == 'POST' and add_location_form.validate():
        add_location_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            add_location_dict = db['Location']
        except:
            print('Error in retrieving form from admin_location.db')

        add_location = admin.Add_location(add_location_form.location1.data, add_location_form.location2.data,  add_location_form.location3.data, add_location_form.location4.data, add_location_form.location5.data)
        add_location_dict[add_location.get_location_Id()] = add_location
        db['Location'] = add_location_dict
        db.close()
        return redirect(url_for('retrieve_location'))
    return render_template('admin_location.html',form=add_location_form)
@app.route('/retrieve_location')
def retrieve_location():
    add_location_dict = {}
    db = shelve.open('storage.db','r' )
    add_location_dict = db['Location']
    db.close()

    add_location_list = []
    for key in add_location_dict:
        admin = add_location_dict.get(key)
        add_location_list.append(admin)
    return render_template('retrieve_location.html', count=len(add_location_list), add_location_list=add_location_list)

@app.route('/updatelocation/<int:id>/', methods=['GET', 'POST'])
def updatelocation(id):
    update_location_form = Add_location(request.form)
    if request.method == 'POST' and update_location_form.validate():
        location_dict = {}
        db = shelve.open('storage.db', 'w')
        location_dict = db['Location']
        location = location_dict.get(id)
        location.set_location1(update_location_form.location1.data)
        location.set_location2(update_location_form.location2.data)
        location.set_location3(update_location_form.location3.data)
        location.set_location4(update_location_form.location4.data)
        location.set_location5(update_location_form.location5.data)
        db['Location'] = location_dict
        db.close()
        return redirect(url_for('retrieve_location'))
    else:
        location_dict = {}
        db = shelve.open('storage.db', 'r')
        location_dict = db['Location']
        db.close()
        location = location_dict.get(id)
        update_location_form.location1.data = location.get_location1()
        update_location_form.location2.data = location.get_location2()
        update_location_form.location3.data = location.get_location3()
        update_location_form.location4.data = location.get_location4()
        update_location_form.location5.data = location.get_location5()
        return render_template('updatelocation.html', form=update_location_form)

# @app.route('/deletelocation/<int:id>', methods=['POST'])
# def deletelocation(id):
#     location_dict = {}
#     db = shelve.open('admin_location.db', 'w')
#     location_dict = db['Location']
#
#     location_dict.pop(id)
#
#     db['Location'] = location_dict
#     db.close()
#     return redirect(url_for('retrieve_location'))
@app.route('/add_time', methods=['GET', 'POST'])
def admin_time():
    add_time_form = Add_time(request.form)
    if request.method == 'POST' and add_time_form.validate():
        add_time_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            add_time_dict = db['Time']
        except:
            print('Error in retrieving form from admin_time.db')

        add_time = admin.Add_time(add_time_form.time1.data, add_time_form.time2.data,add_time_form.time3.data,add_time_form.time4.data,add_time_form.time5.data)
        add_time_dict[add_time.get_time_id()] = add_time
        db['Time'] = add_time_dict
        db.close()
        return redirect(url_for('retrieve_time'))
    return render_template('admin_time.html',form=add_time_form)
@app.route('/retrieve_time')
def retrieve_time():
    add_time_dict = {}
    db = shelve.open('storage.db','r' )
    add_time_dict = db['Time']
    db.close()
    add_time_list = []
    for key in add_time_dict:
        admin = add_time_dict.get(key)
        add_time_list.append(admin)
    return render_template('retrieve_time.html', count=len(add_time_list), add_time_list=add_time_list)

@app.route('/updatetime/<int:id>/', methods=['GET', 'POST'])
def updatetime(id):
    update_time_form = Add_time(request.form)
    if request.method == 'POST' and update_time_form.validate():
        time_dict = {}
        db = shelve.open('storage.db', 'w')
        time_dict = db['Time']
        time = time_dict.get(id)
        time.set_time1(update_time_form.time1.data)
        time.set_time2(update_time_form.time2.data)
        time.set_time3(update_time_form.time3.data)
        time.set_time4(update_time_form.time4.data)
        time.set_time5(update_time_form.time5.data)
        db['Time'] = time_dict
        db.close()
        return redirect(url_for('retrieve_time'))
    else:
        time_dict = {}
        db = shelve.open('storage.db', 'r')
        time_dict = db['Time']
        db.close()
        time = time_dict.get(id)
        update_time_form.time1.data = time.get_time1()
        update_time_form.time2.data = time.get_time2()
        update_time_form.time3.data = time.get_time3()
        update_time_form.time4.data = time.get_time4()
        update_time_form.time5.data = time.get_time5()
        return render_template('updatetime.html', form=update_time_form)
# @app.route('/delete_time/<int:id>', methods=['POST'])
# def delete_time(id):
#     time_dict = {}
#     db = shelve.open('admin_time.db', 'w')
#     time_dict = db['Time']
#
#     time_dict.pop(id)
#     db['Time'] = time_dict
#     db.close()
#     return redirect(url_for('retrieve_time'))

# for staff to enter the
@app.route('/code',methods=['GET', 'POST'])
def code():

    code_form = Code(request.form)
    if request.method == 'POST' and code_form.validate():
        code_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            code_dict = db['Code']
        except:
            print('Error in retrieving form from admin_location.db')

        add_code = booking.Code(1,code_form.small_code.data, code_form.medium_code.data,  code_form.big_code.data, code_form.small_discount.data, code_form.medium_discount.data,code_form.big_discount.data)
        code_dict[add_code.get_Id()] = add_code
        db['Code'] = code_dict
        db.close()
        return redirect(url_for('retrieve'))
    return render_template('code.html',form=code_form)
@app.route('/retrieve')
def retrieve():
    code_dict = {}
    db = shelve.open('storage.db','r' )
    code_dict = db['Code']
    db.close()
    code_list = []
    for key in code_dict:
        admin = code_dict.get(key)
        code_list.append(admin)
    return render_template('retrieve.html', code_list=code_list)
@app.route('/updatecode/<int:id>/', methods=['GET', 'POST'])
def updatecode(id):
    update_code_form = Code(request.form)
    if request.method == 'POST' and update_code_form.validate():
        code_dict = {}
        db = shelve.open('storage.db', 'w')
        code_dict = db['Code']
        code = code_dict.get(id)
        code.set_small_code(update_code_form.small_code.data)
        code.set_medium_code(update_code_form.medium_code.data)
        code.set_big_code(update_code_form.big_code.data)
        code.set_small_discount(update_code_form.small_discount.data)
        code.set_medium_discount(update_code_form.medium_discount.data)
        code.set_big_discount(update_code_form.big_discount.data)
        db['Code'] = code_dict
        db.close()
        return redirect(url_for('retrieve'))
    else:
        code_dict = {}
        db = shelve.open('storage.db', 'r')
        code_dict = db['Code']
        db.close()
        code = code_dict.get(id)
        update_code_form.small_code.data = code.get_small_code()
        update_code_form.medium_code.data = code.get_medium_code()
        update_code_form.big_code.data = code.get_big_code()
        update_code_form.small_discount.data = code.get_small_discount()
        update_code_form.medium_discount.data = code.get_medium_discount()
        update_code_form.big_discount.data = code.get_big_discount()
        return render_template('updatecode.html', form=update_code_form)



@app.route('/purchase/<int:id>/', methods=['GET', 'POST'])
def purchase(id):
    global movie, moviename
    if id == 1:
        movie = movieinfo.MovieInfo("\'demonslayer.web\'",'Demon Slayer', 'PG13: Some Coarese Language','116mins' )
        moviename = movie.get_moviename()
    elif id == 2:
        movie = movieinfo.MovieInfo("samjincompany.webp",'Samjin Company English Class',
                                    'PG13: Some Coarese Language','110 mins' )
        moviename = movie.get_moviename()
    elif id ==3:
        movie = movieinfo.MovieInfo( "horizonline.webp",'Horizon Line', 'NC16: Some Drug scenes','92mins' )
        moviename = movie.get_moviename()
    elif id ==4:
        movie = movieinfo.MovieInfo("thewitches.webp",'The Witches', 'PG13: Some  Frightening Scenes','105mins')
        moviename = movie.get_moviename()
    elif id == 5:
        movie = movieinfo.MovieInfo("voiceofsilence.webp",'Voice of silence', 'PG13: Some Violence','100mins' )
        moviename = movie.get_moviename()
    elif id ==6:
        movie = movieinfo.MovieInfo("honestthief.webp",'Honest Thief', 'PG13: Violence & Brief Coarse','99mins' )
        moviename = movie.get_moviename()
    elif id ==7:
        movie = movieinfo.MovieInfo("kutuk.webp",'Kutuk', 'NC16:Violence & Horror','83mins' )
        moviename = movie.get_moviename()
    elif id ==8:
        movie = movieinfo.MovieInfo("onward.webp",'Disney/Pixar\'s Onwardr', '\'Need Rating\'','102mins' )
        moviename = movie.get_moviename()
    elif id == 9:
        movie = movieinfo.MovieInfo("21bridges.webp",'21 Bridges', '(NC16: Coarse Language & Violence)','99mins' )
        moviename = movie.get_moviename()
    elif id ==  10:
        movie = movieinfo.MovieInfo("pinocchio.webp",'Pinocchio', '(PG: Some Frightening Scenes)','125mins' )
        moviename = movie.get_moviename()
    elif id == 11:
        movie = movieinfo.MovieInfo("youreyestell.webp",'Your Eyes Tell', '(PG13: Some Violence)','123mins' )
        moviename = movie.get_moviename()
    elif id ==12:
        movie = movieinfo.MovieInfo("thewidow.webp",'The widow', '(NC16: Some Nudity & Disturbing Scenes)','86 mins' )
        moviename = movie.get_moviename()
    purchase_form = Purchase(request.form)
    admin_location_dict = {}
    location = shelve.open('storage.db', 'r')
    admin_location_dict = location['Location']
    location.close()
    admin_location_list = []
    for key in admin_location_dict:
        admin = admin_location_dict.get(key)
        admin_location_list.append(admin)
    for location in admin_location_list:
        purchase_form.location.choices = [location.get_location1(),location.get_location2(),location.get_location3(),location.get_location4(),location.get_location5()]

    db = shelve.open('storage.db','r' )
    admin_time_dict = db['Time']
    db.close()
    admin_time_list = []
    for key in admin_time_dict:
        admin = admin_time_dict.get(key)
        admin_time_list.append(admin)
    for time in admin_time_list:
        purchase_form.Time.choices =[time.get_time1(),time.get_time2(),time.get_time3(),time.get_time4(),time.get_time5()]
    if request.method == 'POST' and purchase_form.validate():
        purchase_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            purchase_dict = db['Purchase']
        except:
            print("Error in retrieving form from purchase.db.")
        purchase = booking.Booking(purchase_form.Date.data,purchase_form.Time.data, purchase_form.location.data)
        purchase_dict[1] = purchase
        db['Purchase'] = purchase_dict
        db.close()
        return redirect(url_for('roomtype', id=id))
    return render_template('purchase.html', form=purchase_form, movie=movie)



@app.route('/roomtype/<int:id>/', methods=['GET', 'POST'])
def roomtype(id):
    global movie, moviename
    if id == 1:
        movie = movieinfo.MovieInfo("\'demonslayer.web\'",'Demon Slayer', 'PG13: Some Coarese Language','116mins' )
        moviename = movie.get_moviename()
    elif id == 2:
        movie = movieinfo.MovieInfo("samjincompany.webp",'Samjin Company English Class',
                                    'PG13: Some Coarese Language','110 mins' )
        moviename = movie.get_moviename()
    elif id ==3:
        movie = movieinfo.MovieInfo( "horizonline.webp",'Horizon Line', 'NC16: Some Drug scenes','92mins' )
        moviename = movie.get_moviename()
    elif id ==4:
        movie = movieinfo.MovieInfo("thewitches.webp",'The Witches', 'PG13: Some  Frightening Scenes','105mins')
        moviename = movie.get_moviename()
    elif id == 5:
        movie = movieinfo.MovieInfo("voiceofsilence.webp",'Voice of silence', 'PG13: Some Violence','100mins' )
        moviename = movie.get_moviename()
    elif id ==6:
        movie = movieinfo.MovieInfo("honestthief.webp",'Honest Thief', 'PG13: Violence & Brief Coarse','99mins' )
        moviename = movie.get_moviename()
    elif id ==7:
        movie = movieinfo.MovieInfo("kutuk.webp",'Kutuk', 'NC16:Violence & Horror','83mins' )
        moviename = movie.get_moviename()
    elif id ==8:
        movie = movieinfo.MovieInfo("onward.webp",'Disney/Pixar\'s Onwardr', '\'Need Rating\'','102mins' )
        moviename = movie.get_moviename()
    elif id == 9:
        movie = movieinfo.MovieInfo("21bridges.webp",'21 Bridges', '(NC16: Coarse Language & Violence)','99mins' )
        moviename = movie.get_moviename()
    elif id ==  10:
        movie = movieinfo.MovieInfo("pinocchio.webp",'Pinocchio', '(PG: Some Frightening Scenes)','125mins' )
        moviename = movie.get_moviename()
    elif id == 11:
        movie = movieinfo.MovieInfo("youreyestell.webp",'Your Eyes Tell', '(PG13: Some Violence)','123mins' )
        moviename = movie.get_moviename()
    elif id ==12:
        movie = movieinfo.MovieInfo("thewidow.webp",'The widow', '(NC16: Some Nudity & Disturbing Scenes)','86 mins' )
        moviename = movie.get_moviename()
    roomtype_form = Roomtype(request.form)
    purchase_dict = {}
    db = shelve.open('storage.db', 'r')
    purchase_dict = db['Purchase']
    db.close()
    purchase_list = []
    for key in purchase_dict:
        purchase = purchase_dict.get(key)
        purchase_list.append(purchase)
    for i in purchase_list:
        location = i.get_location()
        time = i.get_Time()
        date = i.get_Date()
    if request.method == 'POST' and roomtype_form.validate():
        roomtype_dict = {}
        room = shelve.open('storage.db', 'c')
        try:
            roomtype_dict = db['Roomtype']
        except:
            print("Error in retrieving form from storage.db.")

        last = 0
        if len(roomtype_dict) == 0:
            new = 1
        else:
            last = list(roomtype_dict.keys())[-1]
            new = last + 1
        lower_upper_alphabet = string.ascii_letters
        l = random.choice(lower_upper_alphabet)
        l2 = random.choice(lower_upper_alphabet)
        ref = "3"+l+"2"+l2
        type = booking.Roomtype(new,ref,roomtype_form.roomtype.data, moviename,date,time,location)
        roomtype_dict[type.get_num()] = type
        room['Roomtype'] = roomtype_dict
        room.close()
        promocode_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            promocode_dict = db['Promo']
        except:
            print("Error in retrieving form from storage.db.")
        num = 1
        promo = booking.Promocode(num,roomtype_form.promocode.data,roomtype_form.roomtype.data)
        promocode_dict[promo.get_Id()] = promo
        db['Promo'] = promocode_dict
        db.close()
        available_dict = {}
        db = shelve.open('storage.db','w')
        try:
            available_dict = db['Available']
        except:
            print('Error in retrieving form from admin_location.db')
        available_keys = []
        for i in available_dict.keys():
            available_keys.append(i)
        for x in available_keys:
            if x.get_location() == purchase_dict.get(1).get_location() and x.get_Time() == purchase_dict.get(1).get_Time() and x.get_Date() == purchase_dict.get(1).get_Date():
                if roomtype_form.roomtype.data == 'Small':
                    s = booking.Minus(available_dict.get(x).get_small_left())
                    left = booking.Left(s.get_minus(),available_dict.get(x).get_medium_left(),available_dict.get(x).get_big_left())
                    available_dict[purchase_dict.get(1)] =left
                    db['Available'] = available_dict

                elif roomtype_form.roomtype.data == 'Medium':
                    m = booking.Minus(available_dict.get(x).get_medium_left())
                    left = booking.Left(available_dict.get(x).get_small_left(),m.get_minus(),available_dict.get(x).get_big_left())
                    available_dict[purchase_dict.get(1)] =left
                    db['Available'] = available_dict

                elif roomtype_form.roomtype.data == 'Big':
                    b = booking.Minus(available_dict.get(x).get_big_left())
                    left = booking.Left(available_dict.get(x).get_small_left(),available_dict.get(x).get_medium_left(),b.get_minus())
                    available_dict[purchase_dict.get(1)] =left
                    db['Available'] = available_dict
            #
            # else:
            #     if roomtype_form.roomtype.data == 'Small':
            #         left = booking.Left(4,5,5)
            #         available_dict[purchase_dict.get(1)] =left
            #         db['Available'] = available_dict
            #
            #     elif roomtype_form.roomtype.data == 'Medium':
            #         left = booking.Left(5,4,5)
            #         available_dict[purchase_dict.get(1)] =left
            #         db['Available'] = available_dict
            #
            #     elif roomtype_form.roomtype.data == 'Big':
            #         left = booking.Left(5,5,4)
            #         available_dict[purchase_dict.get(1)] =left
            #         db['Available'] = available_dict
        db.close()
        return redirect(url_for('checkout'))
    # try:
    #     roomtype_dict = {}
    #     db = shelve.open('storage.db','r')
    #     roomtype_dict = db['Roomtype']
    #     db.close()
    #     room_list = []
    #     for key in roomtype_dict:
    #         room = roomtype_dict.get(key)
    #         room_list.append(room)
    #         small_left = 0
    #         medium_left = 0
    #         big_left = 0
    #         for k in room_list:
    #             for i in purchase_list:
    #                 if i.get_location() == k.get_location() and i.get_Time() == k.get_Time()
    #                 and i.get_Date() == k.get_Date():
    #                     if k.get_roomtype() == 'Small':
    #                         small_left += 1
    #                     elif k.get_roomtype() == 'Medium':
    #                         medium_left += 1
    #                     elif k.get_roomtype() == 'Big':
    #                         big_left += 1
    # except IOError:
    available_dict = {}
    db = shelve.open('storage.db','r')
    available_dict =db['Available']
    db.close()
    available_keys = []
    for i in available_dict.keys():
        available_keys.append(i)
    for x in available_keys:
        if x.get_location() == purchase_dict.get(1).get_location() and x.get_Time() == purchase_dict.get(1).get_Time() and x.get_Date() == purchase_dict.get(1).get_Date():
            room = booking.Left(available_dict.get(x).get_small_left(),available_dict.get(x).get_medium_left(),available_dict.get(x).get_big_left())
        # else:
        #     room = booking.Left(5,5,5)
    return render_template('roomtype.html',room=room, form=roomtype_form, purchase_list=purchase_list, movie=movie)
@app.route('/promocode')
def promocode():
    code_dict = {}
    db = shelve.open('storage.db','r' )
    code_dict = db['Code']
    db.close()
    code_list = []
    for key in code_dict:
        admin = code_dict.get(key)
        code_list.append(admin)
    return render_template('promocode.html',code_list=code_list)
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    code_dict = {}
    db = shelve.open('storage.db','r' )
    code_dict = db['Code']
    db.close()
    code_list = []
    for key in code_dict:
        admin = code_dict.get(key)
        code_list.append(admin)
    promocode_dict = {}
    db = shelve.open('storage.db','r' )
    promocode_dict = db['Promo']
    db.close()
    promocode_list = []
    for key in promocode_dict:
        c = promocode_dict.get(key)
        promocode_list.append(c)
    for x in promocode_list:
        for y in code_list:
            if x.get_roomtype() == 'Small':
                if x.get_promocode() == y.get_small_code():
                    # for the int replace wif get_small_price()
                    discount = 100 - y.get_small_discount()
                    price = 20 * discount/100
                else:
                    price = 20
            elif x.get_roomtype() == 'Medium':
                if x.get_promocode() == y.get_medium_code():
                    discount = 100 - y.get_medium_discount()
                    price = 32 * discount/100
                else:
                    price = 32
            elif x.get_roomtype() == 'Big':
                if x.get_promocode() == y.get_big_code():
                    discount = 100 - y.get_big_discount()
                    price = 42 * discount/100
                else:
                    price = 42

    purchase_dict = {}
    db = shelve.open('storage.db', 'r')
    purchase_dict = db['Purchase']
    db.close()
    roomtype_dict = {}
    db = shelve.open('storage.db','r')
    roomtype_dict = db['Roomtype']
    db.close()
    room_list = []
    for key in roomtype_dict:
        room = roomtype_dict.get(key)
        room_list.append(room)
    for i in room_list:
        if i == room_list[-1]:
            room_type = i.get_roomtype()
        #     roomtype_list = []
        #     for key in roomtype_dict:
        #         roomtype = roomtype_dict.get(key)
        # purchase_list.append(purchase)
    checkout_form = Checkout(request.form)
    if request.method == 'POST' and checkout_form.validate():
        checkout_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            checkout_dict = db['Checkout']
        except:
            print("Error in retrieving form from checkout.db .")
        checkout = payment.Payment(checkout_form.card_number1.data,checkout_form.name_on_card.data,
                                   checkout_form.expiry_month.data, checkout_form.expiry_year.data,
                                   checkout_form.cvv_number.data)
        checkout_dict[checkout.get_cvv_number()] = checkout
        db['Checkout'] = checkout_dict
        db.close()
        return redirect(url_for('booked'))
    return render_template('checkout.html',price =price, room_type=room_type, form=checkout_form, room=room_list)

@app.route('/booked')
def booked():
    purchase_dict = {}
    db = shelve.open('storage.db', 'r')
    purchase_dict = db['Purchase']
    db.close()
    purchase_list = []
    for key in purchase_dict:
        purchase = purchase_dict.get(key)
        purchase_list.append(purchase)
    roomtype_dict = {}
    db = shelve.open('storage.db','r')
    roomtype_dict = db['Roomtype']
    db.close()
    roomtype_list = []
    for key in roomtype_dict:
        roomtype = roomtype_dict.get(key)
        roomtype_list.append(roomtype)
    booked_dict = {}
    db = shelve.open('storage.db', 'c')
    try:
        booked_dict = db['Booked']
    except:
        print("Error in retrieving form from booked.db .")
    for i in purchase_list:
        for k in roomtype_list:
            if i.get_location() == k.get_location() and i.get_Time() == k.get_Time() and i.get_Date() == k.get_Date():
                last = 0
                if len(booked_dict) == 0:
                    new = 1
                else:
                    last = list(booked_dict.keys())[-1]
                    new = last + 1
                booked = booking.Booked(new,k.get_ref(),k.get_moviename(),k.get_Date(),k.get_Time(),k.get_location(),k.get_roomtype())
                booked_dict[booked.get_customerid()] = booked
                db['Booked'] = booked_dict
                db.close()
    return redirect(url_for('success'))
@app.route('/success')
def success():
    booked_dict = {}
    db = shelve.open('storage.db','r' )
    booked_dict = db['Booked']
    db.close()
    booked_list = []
    for key in booked_dict:
        ticket = booked_dict.get(key)
        booked_list.append(ticket)
    for i in booked_list:
        if i == booked_list[-1]:
            movie = i.get_moviename()
    return render_template('success.html',movie=movie, booked_list=booked_list)

@app.route('/ticket')
def ticket():
    booked_dict = {}
    db = shelve.open('storage.db','r' )
    booked_dict = db['Booked']
    db.close()
    booked_list = []
    for key in booked_dict:
        ticket = booked_dict.get(key)
        booked_list.append(ticket)
    return render_template('Tickets.html', count=len(booked_list), purchase_list=booked_list)
@app.route('/view/<int:id>/', methods=['GET', 'POST'])
def view(id):
        booked_dict = {}
        db = shelve.open('storage.db', 'r')
        booked_dict = db['Booked']
        db.close()
        booked = booked_dict.get(id)
        movie = booked.get_moviename()
        Date = booked.get_Date()
        Time = booked.get_Time()
        Location = booked.get_location()
        roomtype = booked.get_roomtype()
        ref = booked.get_ref()
        return render_template('view.html',ref=ref,movie=movie, booked=booked,Date=Date,Time=Time,location=Location,roomtype=roomtype)

# @app.route('/MoviesStaff')
# def moviesstaff():
#     return render_template('moviesstaff.html')
#
#
# @app.route('/staffeditrooms', methods=['GET', 'POST'])
# def staffeditrooms():
#     create_staff_roomform = CreateRoomsForm(request.form)
#     if request.method == 'POST' and create_staff_roomform.validate():
#
#         staff_dict = {}
#         db = shelve.open('storage.db', 'w')
#         db['Staff'] = staff_dict
#
#         #        staff = MoviesStaff.MoviesStaff(create_staff_roomform.room_title.data,
#         #                                        create_staff_roomform.small_roominfo.data,
#         #                                        create_staff_roomform.med_roominfo.data,
#         #                                        create_staff_roomform.large_roominfo.data,
#         #                                        )
#
#         staff = staff_dict.get(id)
#         staff.set_roomtitle(create_staff_roomform.room_title.data)
#         staff.set_small_roominfo(create_staff_roomform.small_roominfo.data)
#         staff.set_med_roominfo(create_staff_roomform.med_roominfo.data)
#         staff.set_large_roominfo(create_staff_roomform.large_roominfo.data)
#
#         #        staff_dict[staff.get_staff_id()] = staff
#         db['Staff'] = staff_dict
#
#         # Test codes
#         #        staff_dict = db['Staff']
#         #        staff = staff_dict[staff.get_staff_id()]
#         #        print("was stored in storage.db successfully with user_id ==", staff.get_user_id())
#
#         db.close()
#
#         return redirect(url_for('home'))
#     else:
#         staff_dict = {}
#         db = shelve.open('storage.db', 'r')
#         db['Staff'] = staff_dict
#         db.close()
#
#         staff = staff_dict.get(id)
#         create_staff_roomform.room_title.data = staff.get_roomtitle()
#         create_staff_roomform.small_roominfo.data = staff.get_small_roominfo()
#         create_staff_roomform.med_roominfo.data = staff.get_med_roominfo()
#         create_staff_roomform.large_roominfo.data = staff.get_large_roominfo()
#
#         staff_list = []
#         for key in staff_dict:
#             staff = staff_dict.get(key)
#             staff_list.append(staff)
#
#         return render_template('editRooms.html', form=create_staff_roomform, staff_list=staff_list)
#
#
# @app.route('/staffeditmovies', methods=['GET', 'POST'])
# def staffeditmovies():
#     create_user_form2 = CreateMoviesForm(request.form)
#     if request.method == 'POST' and create_user_form2.validate():
#         return redirect(url_for('home'))
#     return render_template('editMovies.html', form=create_user_form2)


@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')


@app.route('/Staff')
def staff():
    return render_template('testform.html')

if __name__ == '__main__':
    app.run(debug=True)
