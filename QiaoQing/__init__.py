from flask import Flask,render_template,request, redirect, url_for, send_from_directory, flash, session
#session
import imghdr
import os
from flask_uploads import configure_uploads, patch_request_class
from EditNewestReleases import EditNewestReleasesForm
from EditHomeImage import EditHomeImageForm
from EditHomeDescription import EditHomeDescriptionForm
from EditMovies import UpdateMoviesForm, photos
from EditRooms import CreateRoomsForm
from Forms import CreateUserForm,LoginForm, RegisterForm, Purchase, Add_time, Add_location, Roomtype
from checkoutform import Checkout
import MovieInfoToTicket as MITT
import admin as admin
from pathlib import Path

import shelve, RoomInfo, MovieInfo, UserId, User, HomeDescription, HomeImage, NewestReleases, payment, booking, random, string
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'uploads')
app.config['UPLOAD_EXTENSIONS'] = ['.jfif','.webp','.jpg','.png','.gif']
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

configure_uploads(app, photos)
patch_request_class(app)

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

@app.route('/Purchase/<int:movieid>/', methods=['GET', 'POST'])
def purchase(movieid):
    purchase_form = Purchase(request.form)

    movieinfo_dict = {}
    db = shelve.open('movieinfostorage.db', 'r')
    movieinfo_dict = db['MovieInfo']
    movieinfo = movieinfo_dict.get(movieid)
    db.close()

    admin_location_dict = {}
    db = shelve.open('storage.db', 'r')
    admin_location_dict = db['Location']
    db.close()

    admin_location_list = []
    for key in admin_location_dict:
        admin = admin_location_dict.get(key)
        admin_location_list.append(admin)

    for location in admin_location_list:
        purchase_form.location.choices = [location.get_location1(),location.get_location2(),location.get_location3(),location.get_location4(),location.get_location5()]

    admin_time_dict = {}
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

        purchase = booking.Booking(purchase_form.Date.data
                                   ,purchase_form.Time.data
                                   ,purchase_form.location.data)

        if len(purchase_dict) == 0:
            currentpurchaseid = 1
        else: #1:movieinfo
            last = list(movieinfo_dict.keys())[-1]
            currentpurchaseid = last + 1

        purchase.set_BookDateTimeLocationID(currentpurchaseid)
        purchaseid = purchase.get_BookDateTimeLocationID()
        purchase_dict[purchase.get_BookDateTimeLocationID()] = purchase
        db['Purchase'] = purchase_dict
        db.close()

        return redirect(url_for('roomtype', purchaseid=purchaseid, movieid=movieid))
    return render_template('purchase.html', form=purchase_form, movieinfo=movieinfo)

@app.route('/Createsroomtype')
def Createroomtype():

    bookingleft_dict = {}
    db = shelve.open('storage.db', 'c')
    try:
        bookingleft_dict = db["BookingLeft"]
    except:
        print("Error in retrieving storage.db.")

    room16Jan = booking.Left("16Jan")
    room17Jan = booking.Left("17Jan")
    room18Jan = booking.Left("18Jan")
    room19Jan = booking.Left("19Jan")
    room20Jan = booking.Left("20Jan")

    bookingleft_dict[room16Jan.get_LeftID()] = room16Jan
    bookingleft_dict[room17Jan.get_LeftID()] = room17Jan
    bookingleft_dict[room18Jan.get_LeftID()] = room18Jan
    bookingleft_dict[room19Jan.get_LeftID()] = room19Jan
    bookingleft_dict[room20Jan.get_LeftID()] = room20Jan

    db["BookingLeft"] = bookingleft_dict

    # Test codes
    bookingleft_dict = db["BookingLeft"] #Value of Staff Key in Storage
    room20Jan = bookingleft_dict[room16Jan.get_LeftID()] #value of Value of Staff Key in Storage
    print("was stored in storage.mb successfully with user_id ==", room20Jan.get_LeftID())

    db.close()

@app.route('/roomtype/<int:movieid>/<int:purchaseid>/', methods=['GET', 'POST'])
def roomtype(movieid,purchaseid):
    roomtype_form = Roomtype(request.form)

    movieinfo_dict = {}
    db = shelve.open('movieinfostorage.db', 'r')
    movieinfo_dict = db['MovieInfo']
    db.close()

    movieinfo = movieinfo_dict.get(movieid) #specific object

    purchase_dict = {}
    db = shelve.open('storage.db', 'r')
    purchase_dict = db['Purchase']
    db.close()

    purchaseinfo = purchase_dict.get(purchaseid)

    moviename = movieinfo.get_moviename()
    location = purchaseinfo.get_location()
    time = purchaseinfo.get_Time()
    date = purchaseinfo.get_Date()

    if request.method == 'POST' and roomtype_form.validate():
        roomtype_dict = {}
        room = shelve.open('storage.db', 'c')

        try:
            roomtype_dict = db['Roomtype']
        except:
            print("Error in retrieving form from storage.db.")

        if len(roomtype_dict) == 0:
            new = 1
        else:
            last = list(roomtype_dict.keys())[-1]
            new = last + 1

        lower_upper_alphabet = string.ascii_letters
        l = random.choice(lower_upper_alphabet)
        l2 = random.choice(lower_upper_alphabet)
        ref = "3"+l+"2"+l2

        type = booking.Roomtype(new,
                                ref,
                                roomtype_form.roomtype.data,
                                moviename,
                                date,
                                time,
                                location)

        roomtypeid = type.get_num()
        roomtype_dict[roomtypeid] = type
        room['Roomtype'] = roomtype_dict
        room.close()

        roomtype_dict = {}
        db = shelve.open('storage.db', 'r')
        roomtype_dict = db['Roomtype']
        db.close()

        roomtypeinfo = roomtype_dict.get(roomtypeid) #specific object

        return redirect(url_for('checkout', roomtypeinfo=roomtypeinfo, movieinfo=movieinfo, purchaseinfo=purchaseinfo, purchaseid=purchaseid, movieid=movieid, roomtypeid=roomtypeid))

    roomtype_dict = {}
    db = shelve.open('storage.db','r')
    roomtype_dict = db['Roomtype']
    db.close()

    roomtype_list = []
    for key in roomtype_dict:
        room = roomtype_dict.get(key)
        roomtype_list.append(room)

    purchase_dict = {}
    db = shelve.open('storage.db', 'r')
    purchase_dict = db['Purchase']
    db.close()

    purchase_list = []
    for key in purchase_dict:
        purchase = purchase_dict.get(key)
        purchase_list.append(purchase)

    GetDate = purchaseinfo.get_Date()
    DateGotten = 0

    if GetDate == "16/01/2021":
        DateGotten = "16Jan"

    if GetDate == "17/01/2021":
        DateGotten = "17Jan"

    if GetDate == "18/01/2021":
        DateGotten = "18Jan"

    if GetDate == "19/01/2021":
        DateGotten = "19Jan"

    if GetDate == "20/01/2021":
        DateGotten = "20Jan"

    bookingleft_dict = {}
    db = shelve.open('storage.db', 'r')
    bookingleft_dict = db["BookingLeft"]
    db.close()

    bookingleft_list = []
    for key in bookingleft_dict:
        bookingleft = bookingleft_dict.get(key)
        bookingleft_list.append(bookingleft)

    for k in roomtype_list:
        for i in purchase_list:
            if i.get_location() == k.get_location() \
                    and i.get_Time() == k.get_Time() \
                    and i.get_Date() == k.get_Date():

                bookingleft_dict = {}
                db = shelve.open('storage.db', 'w')
                bookingleft_dict = db["BookingLeft"]
                db.close()

                existingbooking = bookingleft_list[DateGotten]
                small_left = existingbooking.get_small_left()
                med_left = existingbooking.get_medium_left()
                big_left = existingbooking.get_big_left()

                if k.get_roomtype() == 'Small':
                    small_left += 1
                existingbooking.set_small_left(small_left)

                if k.get_roomtype() == 'Medium':
                    med_left += 1
                existingbooking.set_medium_left(med_left)

                if k.get_roomtype() == 'Big':
                    big_left += 1
                existingbooking.set_big_left(big_left)

    return render_template('roomtype.html'
                           ,roomtype_list = roomtype_list
                           , purchase_list=purchase_list
                            , movieid = movieid
                            , purchaseid = purchaseid
                           ,room=room, form=roomtype_form)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
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
    return render_template('checkout.html',room_type=room_type, form=checkout_form, room=room_list)

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

class CuUser(UserMixin):
    id = 0

    def __init__(self, username, gender, email, password):
        CuUser.id += 1
        self.id = CuUser.id
        self.username = username
        self.gender = gender
        self.email = email
        self.password = password

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def __repr__(self):
        return f'<CuUser: {self.username}>'

@login_manager.user_loader
def load_user(user_id):
    return CuUser.get_id(user_id)

@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm(request.form)
    if request.method == 'POST' and register_form.validate():
        users_dict = {}
        db = shelve.open('users.db', 'c')
        try:
            users_dict = db['Users']
        except:
            print('Error in retrieving Users from users.db')

        email = register_form.email.data
        if email in users_dict:
            flash('You have already registered with the existing email.', 'Danger')
            return redirect(url_for('login'))
        else:
            hashed_password = generate_password_hash(register_form.password.data, method='sha256')
            user = CuUser(
                register_form.username.data,
                register_form.gender.data,
                register_form.email.data,
                hashed_password)
            users_dict[int(user.get_id())] = user
            db['Users'] = users_dict

            db.close()
            flash('You have successfully registered', 'success')

            return redirect(url_for('login'))
    return render_template('register.html', form=register_form)


@app.route('/profile')
def profile():
    users_dict = {}
    db = shelve.open('users.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)
    return render_template('profile.html', count=len(users_list), users_list=users_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        users_dict = {}
        db = shelve.open('users.db',  'r')
        users_dict = db['Users']
        db.close()
        users_list = []
        for id in users_dict:
            user = users_dict.get(id)
            users_list.append(user)
        for user in users_list:
            if user.email == login_form.email.data:
                #password = generate_password_hash(login_form.password.data, method='sha256')
                check_password_hash(user.password, login_form.password.data)
                if check_password_hash(user.password, login_form.password.data) == True:
                    session['id'] = True
                    session['login'] = user.id
                    session['loggedIn'] = user.username
                    return redirect(url_for('homecustomer',userid=session['login']))
                else:
                    flash("Incorrect Password.",'warning')
    return render_template('login.html', form=login_form)

def LoginedUser():
    LoginedUser_dict = {}
    loginuser = shelve.open('loginuserstorage.db', 'c')

    try:
        LoginedUser_dict = loginuser['Users']
    except:
        print('Error in retrieving Users from storage.db.')

    LoginedUserID = UserId.UserId("Staff")
    LoginedUser_dict[LoginedUserID.get_UserID()] = LoginedUserID
    loginuser['Users'] = LoginedUser_dict

    # Test codes
    LoginedUser_dict = loginuser['Users']
    LoginedUserID = LoginedUser_dict[LoginedUserID.get_UserID()]
    print(LoginedUserID.get_UserID(), 'was stored in storage.db successfully with user_id ==', LoginedUserID.get_UserID())
    loginuser.close()


@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    update_form = RegisterForm(request.form)
    if request.method == 'POST':
        users_dict = {}
        db = shelve.open('users.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.username = update_form.username.data
        user.email = update_form.email.data
        user.gender = update_form.gender.data

        db['Users'] = users_dict
        db.close()
        return redirect(url_for('profile'))

    else:
        users_dict = {}
        db = shelve.open('users.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_form.username.data = user.username
        update_form.email.data = user.email
        update_form.gender.data = user.gender

        return render_template('update.html', form=update_form)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    users_dict = {}
    db = shelve.open('users.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()
    session.pop('login')
    return redirect(url_for('homecustomer'))

@app.route('/logout')
def logout():
    session.pop('login',None)
    return redirect(url_for('homecustomer'))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
@app.route('/<userid>')
def homecustomer(userid=None):
    homeimage_dict = {}
    db = shelve.open('homeimagestorage.db', 'r')
    homeimage_dict = db['HomeImage']
    db.close()

    homedescription_dict = {}
    db = shelve.open('homedescriptionstorage.db', 'r')
    homedescription_dict = db['HomeDescription']
    db.close()

    newreleases_dict = {}
    db = shelve.open('newreleasesinfostorage.db', 'r')
    newreleases_dict = db['NewReleases']
    db.close()

    homeimage_list = []
    for key in homeimage_dict:
        homeimage = homeimage_dict.get(key)
        homeimage_list.append(homeimage)

    homedescription_list = []
    for key in homedescription_dict:
        homedescription = homedescription_dict.get(key)
        homedescription_list.append(homedescription)

    newreleases_list = []
    for key in newreleases_dict:
        newreleases = newreleases_dict.get(key)
        newreleases_list.append(newreleases)

    session['login'] = userid

    return render_template('homecustomer.html',userid=userid,homedescription_list=homedescription_list,homeimage_list=homeimage_list,newreleases_list=newreleases_list)

def joinPath(param, file):
    pass

@app.route('/EditHomeDescription/<userid>/<homeid>/', methods=['GET', 'POST'])
def EditHomeDescription(userid,homeid):
    edithomedescription = EditHomeDescriptionForm(request.form)
    if request.method == 'POST' and edithomedescription.validate():

        homedescription_dict = {}
        db = shelve.open('homedescriptionstorage.db', 'w')
        homedescription_dict = db['HomeDescription']

        homedescription = homedescription_dict.get(homeid)
        print(homedescription)

        homedescription.set_homedescription(edithomedescription.home_description.data)

        db['HomeDescription'] = homedescription_dict
        db.close()

        session['login'] = userid

        return redirect(url_for('homecustomer',userid=session['login']))

    else:
        homedescription_dict = {}
        db = shelve.open('homedescriptionstorage.db', 'r')
        homedescription_dict = db['HomeDescription']
        db.close()

        homedescription = homedescription_dict.get(homeid)
        edithomedescription.home_description.data = homedescription.get_homedescription()

        return render_template('EditHomeDescription.html', form=edithomedescription)

@app.route('/EditHomeImage/<userid>/<homeid>/', methods=['GET', 'POST'])
def EditHomeImage(userid,homeid):
    edithomeimage = EditHomeImageForm(CombinedMultiDict((request.files, request.form)))
#    file_url = send_from_directory(app.config['UPLOAD_FOLDER'],filename)
    if edithomeimage.validate():
        filename1 = secure_filename(edithomeimage.home_image.data.filename)
        filename2 = secure_filename(edithomeimage.home_policy_image.data.filename)

        if filename1 != '' or filename2 != '':
            file_ext1 = os.path.splitext(filename1)[1]
            file_ext2 = os.path.splitext(filename2)[1]

            if file_ext1 not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext1 != validate_image(edithomeimage.home_image.data.stream):
                return "Invalid Image",400
            elif file_ext2 not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext2 != validate_image(edithomeimage.home_policy_image.data.stream):
                return "Invalid Image",400

            else:
                edithomeimage.home_image.data.save(os.path.join(basedir, 'uploads', filename1))
                edithomeimage.home_policy_image.data.save(os.path.join(basedir, 'uploads', filename2))

                homeimage_dict = {}
                db = shelve.open('homeimagestorage.db', 'w')
                homeimage_dict = db['HomeImage']

                homeimage = homeimage_dict.get(homeid)
                homeimage.set_homeimage(filename1)
                homeimage.set_homepolicy(edithomeimage.home_policy.data)
                homeimage.set_homepolicyimage(filename2)

                db['HomeImage'] = homeimage_dict
                db.close()

                session['login'] = userid
                return redirect(url_for('homecustomer',userid=session['login']))

    else:
        homeimage_dict = {}
        db = shelve.open('homeimagestorage.db', 'r')
        homeimage_dict = db['HomeImage']

        homeimage = homeimage_dict.get(homeid)
        edithomeimage.home_image.data = homeimage.get_homeimage()
        edithomeimage.home_policy.data = homeimage.get_homepolicy()
        edithomeimage.home_policy_image.data = homeimage.get_homepolicyimage()

    return render_template('EditHomeImage.html', form=edithomeimage)

@app.route('/EditNewestReleases/<userid>/<homeid>/', methods=['GET', 'POST'])
def EditNewestReleases(userid,homeid):
    editnewestreleases = EditNewestReleasesForm(CombinedMultiDict((request.files, request.form)))
    if editnewestreleases.validate():
        filename1 = secure_filename(editnewestreleases.release_image1.data.filename)
        filename2 = secure_filename(editnewestreleases.release_image2.data.filename)
        filename3 = secure_filename(editnewestreleases.release_image3.data.filename)
        filename4 = secure_filename(editnewestreleases.release_image4.data.filename)

        if filename1 != '' or filename2 != '' or filename3 != '' or filename4 != '':
            file_ext1 = os.path.splitext(filename1)[1]
            file_ext2 = os.path.splitext(filename2)[1]
            file_ext3 = os.path.splitext(filename3)[1]
            file_ext4 = os.path.splitext(filename4)[1]

            if file_ext1 not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext1 != validate_image(editnewestreleases.release_image1.data.stream):
                return "Invalid Image",400
            elif file_ext2 not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext2 != validate_image(editnewestreleases.release_image2.data.stream):
                return "Invalid Image",400
            elif file_ext3 not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext3 != validate_image(editnewestreleases.release_image3.data.stream):
                return "Invalid Image",400
            elif file_ext4 not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext4 != validate_image(editnewestreleases.release_image4.data.stream):
                return "Invalid Image",400
            else:
                editnewestreleases.release_image1.data.save(os.path.join(basedir, 'uploads', filename1))
                editnewestreleases.release_image2.data.save(os.path.join(basedir, 'uploads', filename2))
                editnewestreleases.release_image3.data.save(os.path.join(basedir, 'uploads', filename3))
                editnewestreleases.release_image4.data.save(os.path.join(basedir, 'uploads', filename4))

                newreleasesinfo_dict = {}
                db = shelve.open('newreleasesinfostorage.db', 'w')
                newreleasesinfo_dict = db['NewReleases']
                newreleasesinfo = newreleasesinfo_dict.get(homeid)
                newreleasesinfo.set_release_image1(filename1)
                newreleasesinfo.set_release_name1(editnewestreleases.release_name1.data)
                newreleasesinfo.set_release_image2(filename2)
                newreleasesinfo.set_release_name2(editnewestreleases.release_name2.data)
                newreleasesinfo.set_release_image3(filename3)
                newreleasesinfo.set_release_name3(editnewestreleases.release_name3.data)
                newreleasesinfo.set_release_image4(filename4)
                newreleasesinfo.set_release_name4(editnewestreleases.release_name4.data)

                db['NewReleases'] = newreleasesinfo_dict
                db.close()
                session['login'] = userid
                return redirect(url_for('homecustomer',userid=session['login']))
    else:
        newreleasesinfo_dict = {}
        db = shelve.open('newreleasesinfostorage.db', 'r')
        newreleasesinfo_dict = db['NewReleases']

        newreleases = newreleasesinfo_dict.get(homeid)
        editnewestreleases.release_image1.data = newreleases.get_release_image1()
        editnewestreleases.release_name1.data = newreleases.get_release_name1()
        editnewestreleases.release_image2.data = newreleases.get_release_image2()
        editnewestreleases.release_name2.data = newreleases.get_release_name2()
        editnewestreleases.release_image3.data = newreleases.get_release_image3()
        editnewestreleases.release_name3.data = newreleases.get_release_name3()
        editnewestreleases.release_image4.data = newreleases.get_release_image4()
        editnewestreleases.release_name4.data = newreleases.get_release_name4()

    return render_template('EditNewReleases.html', form=editnewestreleases)

@app.route('/MoviesCustomer/None/')
@app.route('/MoviesCustomer/<userid>')
def moviescustomer(userid=None):

    users_dict = {}
    db = shelve.open('users.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    movieinfo_dict = {}
    db = shelve.open('movieinfostorage.db', 'r')
    movieinfo_dict = db['MovieInfo']
    db.close()

    roominfo_dict = {}
    db = shelve.open('roominfostorage.db', 'r')
    roominfo_dict = db['RoomInfo']
    db.close()

    movieinfo_list = []
    for key in movieinfo_dict:
        movieinfo = movieinfo_dict.get(key)
        movieinfo_list.append(movieinfo)

    roominfo_list = []
    for key in roominfo_dict:
        roominfo = roominfo_dict.get(key)
        roominfo_list.append(roominfo)

    #maybe use dict?
    image_list = os.listdir(app.config['UPLOADED_PHOTOS_DEST'])
    print(image_list)

    session['login'] = userid

    return render_template('moviescustomer.html', moviecount=len(movieinfo_list)
                   ,roomcount=len(roominfo_list) ,imagecount=len(image_list)
                   ,movieinfo_list=movieinfo_list ,roominfo_list=roominfo_list
                   ,image_list=image_list, users_list=users_list,userid=userid)

@app.route('/EditRooms/<userid>/<id>/', methods=['GET', 'POST'])
def EditRooms(userid,id):
    room_form = CreateRoomsForm(CombinedMultiDict((request.files, request.form)))
#    file_url = send_from_directory(app.config['UPLOAD_FOLDER'],filename)
    if room_form.validate():
        filename1 = secure_filename(room_form.small_roomimage1.data.filename)
        filename2 = secure_filename(room_form.small_roomimage2.data.filename)
        filename3 = secure_filename(room_form.med_roomimage.data.filename)
        filename4 = secure_filename(room_form.large_roomimage1.data.filename)
        filename5 = secure_filename(room_form.large_roomimage2.data.filename)

        if filename1 != '' or filename2 != '' or filename3 != '' or filename4 != '' or filename5 != '':
            file_ext1 = os.path.splitext(filename1)[1]
            file_ext2 = os.path.splitext(filename2)[1]
            file_ext3 = os.path.splitext(filename3)[1]
            file_ext4 = os.path.splitext(filename4)[1]
            file_ext5 = os.path.splitext(filename5)[1]

            if file_ext1 not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext1 != validate_image(room_form.small_roomimage1.data.stream):
                return "Invalid Image",400
            elif file_ext2 not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext2 != validate_image(room_form.small_roomimage2.data.stream):
                return "Invalid Image",400
            elif file_ext3 not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext3 != validate_image(room_form.med_roomimage.data.stream):
                return "Invalid Image",400
            elif file_ext4 not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext4 != validate_image(room_form.large_roomimage1.data.stream):
                return "Invalid Image",400
            elif file_ext5 not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext5 != validate_image(room_form.large_roomimage2.data.stream):
                return "Invalid Image",400
            else:
                room_form.small_roomimage1.data.save(os.path.join(basedir, 'uploads', filename1))
                room_form.small_roomimage1.data.save(os.path.join(basedir, 'uploads', filename2))
                room_form.med_roomimage.data.save(os.path.join(basedir, 'uploads', filename3))
                room_form.large_roomimage1.data.save(os.path.join(basedir, 'uploads', filename4))
                room_form.large_roomimage2.data.save(os.path.join(basedir, 'uploads', filename5))

                roominfo_dict = {}
                db = shelve.open('roominfostorage.db', 'w')
                roominfo_dict = db['RoomInfo']

                roominfo = roominfo_dict.get(id)

                roominfo.set_roomtitle(room_form.room_title.data)
                roominfo.set_small_roominfo(room_form.small_roominfo.data)
                roominfo.set_small_roomprice(room_form.small_roomprice.data)
                roominfo.set_small_roomimage1(filename1)
                roominfo.set_small_roomimage2(filename2)
                roominfo.set_med_roominfo(room_form.med_roominfo.data)
                roominfo.set_med_roomprice(room_form.med_roomprice.data)
                roominfo.set_med_roomimage(filename3)
                roominfo.set_large_roominfo(room_form.large_roominfo.data)
                roominfo.set_large_roomprice(room_form.large_roomprice.data)
                roominfo.set_large_roomimage1(filename4)
                roominfo.set_large_roomimage2(filename5)
                roominfo.set_gvexclusivesmall_roominfo(room_form.gvexclusivesmall_roominfo.data)
                roominfo.set_gvexclusivesmall_roomprice(room_form.gvexclusivesmall_roomprice.data)
                roominfo.set_gvexclusivemed_roominfo(room_form.gvexclusivemed_roominfo.data)
                roominfo.set_gvexclusivemed_roomprice(room_form.gvexclusivemed_roomprice.data)
                roominfo.set_gvexclusivelarge_roominfo(room_form.gvexclusivelarge_roominfo.data)
                roominfo.set_gvexclusivelargeroomprice(room_form.gvexclusivelargeroomprice.data)

                db['RoomInfo'] = roominfo_dict
                db.close()
                session['login'] = userid

                return redirect(url_for('moviescustomer',userid=session['login']))

    else:
        roominfo_dict = {}
        db = shelve.open('roominfostorage.db', 'w')
        roominfo_dict = db['RoomInfo']

        roominfo = roominfo_dict.get(id)
        room_form.room_title.data = roominfo.get_roomtitle()
        room_form.small_roominfo.data = roominfo.get_small_roominfo()
        room_form.small_roomprice.data = roominfo.get_small_roomprice()
        room_form.med_roominfo.data = roominfo.get_med_roominfo()
        room_form.med_roomprice.data = roominfo.get_med_roomprice()
        room_form.large_roominfo.data = roominfo.get_large_roominfo()
        room_form.large_roomprice.data = roominfo.get_large_roomprice()
        room_form.gvexclusivesmall_roominfo.data = roominfo.get_gvexclusivesmall_roominfo()
        room_form.gvexclusivesmall_roomprice.data = roominfo.get_gvexclusivesmall_roomprice()
        room_form.gvexclusivemed_roominfo.data = roominfo.get_gvexclusivemed_roominfo()
        room_form.gvexclusivemed_roomprice.data = roominfo.get_gvexclusivemed_roomprice()
        room_form.gvexclusivelarge_roominfo.data = roominfo.get_gvexclusivelarge_roominfo()
        room_form.gvexclusivelargeroomprice.data = roominfo.get_gvexclusivelargeroomprice()
        room_form.small_roomimage1.data = roominfo.get_small_roomimage1()
        room_form.small_roomimage2.data = roominfo.get_small_roomimage2()
        room_form.med_roomimage.data = roominfo.get_med_roomimage()
        room_form.large_roomimage1.data = roominfo.get_large_roomimage1()
        room_form.large_roomimage2.data = roominfo.get_large_roomimage2()

    return render_template('editRooms.html', form=room_form)

@app.route('/ChooseMovies')
def ChooseMovies():
    movieinfo_dict = {}
    db = shelve.open('movieinfostorage.db', 'r')
    movieinfo_dict = db['MovieInfo']
    db.close()

    movieinfo_list = []
    for key in movieinfo_dict:
        movieinfo = movieinfo_dict.get(key)
        movieinfo_list.append(movieinfo)

    userid = session['login']

    return render_template('chooseMovies.html',userid=userid,movieinfo_list=movieinfo_list)

@app.route('/MoviesStaff/<filename>')
def send_image(filename):
    return send_from_directory("uploads",filename)

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413

@app.route('/CreateMovies/<userid>', methods=['GET', 'POST'])
def CreateMovies(userid):
    create_movieform = UpdateMoviesForm(CombinedMultiDict((request.files, request.form)))
#    file_url = send_from_directory(app.config['UPLOAD_FOLDER'],filename)
    if create_movieform.validate():
        filename = secure_filename(create_movieform.movie_image.data.filename)

        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext != validate_image(create_movieform.movie_image.data.stream):
                return "Invalid Image",400
            else:
                create_movieform.movie_image.data.save(os.path.join(basedir, 'uploads', filename))

                movieinfo_dict = {}
                db = shelve.open('movieinfostorage.db', 'c')

                try:
                    movieinfo_dict = db['MovieInfo']
                except:
                    print("Error in retrieving Movies from movieinfostorage.db.")

                movieinfo = MovieInfo.MovieInfo(
                                            filename,
                                            create_movieform.movie_name.data,
                                            create_movieform.movieagerating.data,
                                            create_movieform.movieduration.data,
                                            create_movieform.gvexclusivetag.data,
                                            create_movieform.movieHorror.data,
                                            create_movieform.movieDrama.data,
                                            create_movieform.movieComedy.data,
                                            create_movieform.movieScience.data,
                                            create_movieform.movieRomance.data,
                                            create_movieform.movieAnimation.data,
                                            create_movieform.movieCrimeFilm.data,
                                            create_movieform.movieThriller.data,
                                            create_movieform.movieAdventure.data,
                                            create_movieform.movieEmotional.data,
                                            create_movieform.movieMystery.data,
                                            create_movieform.movieAction.data)

                if len(movieinfo_dict) == 0:
                    currentmovieid = 1
                else: #1:movieinfo
                    last = list(movieinfo_dict.keys())[-1]
                    currentmovieid = last + 1

                movieinfo.set_movie_id(currentmovieid)
                movieinfo_dict[movieinfo.get_movie_id()] = movieinfo
                db['MovieInfo'] = movieinfo_dict

            # Test codes
            movieinfo_dict = db['MovieInfo'] #Value of Staff Key in Storage
            movieinfo = movieinfo_dict[movieinfo.get_movie_id()] #value of Value of Staff Key in Storage
            print("was stored in storage.mb successfully with user_id ==", movieinfo.get_movie_id())

            db.close()

            session['login'] = userid

        return redirect(url_for('moviescustomer', userid = session['login'] ,filename=filename))
    return render_template('createMovie.html', userid=userid , form=create_movieform)

@app.route('/UpdateMovie/<userid>/<int:id>/', methods=['GET', 'POST'])
def UpdateMovie(userid,id):
    update_movieform = UpdateMoviesForm(CombinedMultiDict((request.files, request.form)))
    if update_movieform.validate():
        filename = secure_filename(update_movieform.movie_image.data.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext != validate_image(update_movieform.movie_image.data.stream):
                return "Invalid Image",400
            else:
                update_movieform.movie_image.data.save(os.path.join(basedir, 'uploads', filename))

                movieinfo_dict = {}
                db = shelve.open('movieinfostorage.db', 'w')
                movieinfo_dict = db['MovieInfo']

                movie = movieinfo_dict.get(id)
                print(movie)
                movie.set_movieimage(filename)
                movie.set_moviename(update_movieform.movie_name.data)
                movie.set_movieagerating(update_movieform.movieagerating.data)
                movie.set_movieduration(update_movieform.movieduration.data)
                movie.set_gvexclusivetag(update_movieform.gvexclusivetag.data)
                movie.set_movieHorror(update_movieform.movieHorror.data)
                movie.set_movieDrama(update_movieform.movieDrama.data)
                movie.set_movieComedy(update_movieform.movieComedy.data)
                movie.set_movieScience(update_movieform.movieScience.data)
                movie.set_movieRomance(update_movieform.movieRomance.data)
                movie.set_movieAnimation(update_movieform.movieAnimation.data)
                movie.set_movieCrimeFilm(update_movieform.movieCrimeFilm.data)
                movie.set_movieThriller(update_movieform.movieThriller.data)
                movie.set_movieAdventure(update_movieform.movieAdventure.data)
                movie.set_movieEmotional(update_movieform.movieEmotional.data)
                movie.set_movieMystery(update_movieform.movieMystery.data)
                movie.set_movieAction(update_movieform.movieAction.data)

                db['MovieInfo'] = movieinfo_dict
                db.close()

                session['login'] = userid

                return redirect(url_for('moviescustomer',userid=session['login']))
    else:
        movieinfo_dict = {}
        db = shelve.open('movieinfostorage.db', 'r')
        movieinfo_dict = db['MovieInfo']
        db.close()

        movie = movieinfo_dict.get(id)
        update_movieform.movie_image.data = movie.get_movieimage()
        update_movieform.movie_name.data = movie.get_moviename()
        update_movieform.movieagerating.data = movie.get_movieagerating()
        update_movieform.movieduration.data = movie.get_movieduration()
        update_movieform.gvexclusivetag.data = movie.get_gvexclusivetag()
        update_movieform.movieHorror.data = movie.get_movieHorror()
        update_movieform.movieDrama.data = movie.get_movieDrama()
        update_movieform.movieComedy.data = movie.get_movieComedy()
        update_movieform.movieScience.data = movie.get_movieScience()
        update_movieform.movieRomance.data = movie.get_movieRomance()
        update_movieform.movieAnimation.data = movie.get_movieAnimation()
        update_movieform.movieCrimeFilm.data = movie.get_movieCrimeFilm()
        update_movieform.movieThriller.data = movie.get_movieThriller()
        update_movieform.movieAdventure.data = movie.get_movieAdventure()
        update_movieform.movieEmotional.data = movie.get_movieEmotional()
        update_movieform.movieMystery.data = movie.get_movieMystery()
        update_movieform.movieAction.data = movie.get_movieAction()

        return render_template('updateMovie.html', form=update_movieform)

@app.route('/DeleteMovie/<userid>/<int:id>/', methods=['POST'])
def DeleteMovie(userid,id):
    movieinfo_dict = {}
    db = shelve.open('movieinfostorage.db', 'w')
    movieinfo_dict = db['MovieInfo']

    movieinfo_dict.pop(id)

    db['MovieInfo'] = movieinfo_dict
    db.close()

    session['login'] = userid

    return redirect(url_for('moviesstaff',userid=userid,id=id))

@app.route('/Filter')
def moviesfilter():
    movieinfo_dict = {}
    db = shelve.open('movieinfostorage.db', 'r')
    movieinfo_dict = db['MovieInfo']
    db.close()

    roominfo_dict = {}
    db = shelve.open('roominfostorage.db', 'r')
    roominfo_dict = db['RoomInfo']
    db.close()

    movieinfo_list = []
    for key in movieinfo_dict:
        movieinfo = movieinfo_dict.get(key)
        movieinfo_list.append(movieinfo)

    roominfo_list = []
    for key in roominfo_dict:
        roominfo = roominfo_dict.get(key)
        roominfo_list.append(roominfo)

    image_list = os.listdir(app.config['UPLOADED_PHOTOS_DEST'])
    print(image_list)
    return render_template('moviesfilter.html', movieinfo_list=movieinfo_list,  roominfo_list=roominfo_list, image_list=image_list)

@app.route('/Review/<userid>')
def Review(userid=None):
    session['login'] = userid
    return render_template('contactUs.html',userid=userid)

@app.route('/contactUs/None/')
@app.route('/contactUs/<userid>')
def contact_us(userid=None):
    session['login'] = userid
    return render_template('contactUs.html',userid=userid)

@app.route('/createQuestion', methods=['GET', 'POST'])
def create_question():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from storage.db.")

        user = User.User(create_user_form.Question.data, create_user_form.Answer.data, create_user_form.Availability.data, create_user_form.NumberOfPeople.data, create_user_form.remarks.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_questions'))
    return render_template('createQuestion.html', form=create_user_form)

@app.route('/retrieveQuestion')
def retrieve_questions():
    users_dict = {}
    db = shelve.open('storage.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('retrieveQuestions.html',count=len(users_list), users_list=users_list)


@app.route('/updateQuestion/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('storage.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_Question(update_user_form.Question.data)
        user.set_Answer(update_user_form.Answer.data)
        user.set_Availability(update_user_form.Availability .data)
        user.set_NumberOfPeople(update_user_form.NumberOfPeople.data)
        user.set_remarks(update_user_form.remarks.data)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_questions'))
    else:
        users_dict = {}
        db = shelve.open('storage.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.Question.data = user.get_Question()
        update_user_form.Answer.data = user.get_Answer()
        update_user_form.Availability.data = user.get_Availability()
        update_user_form.NumberOfPeople.data = user.get_NumberOfPeople()
        update_user_form.remarks.data = user.get_remarks()

        return render_template('updateQuestions.html', form=update_user_form)

@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
        users_dict = {}
        db = shelve.open('storage.db', 'w')
        users_dict = db['Users']

        users_dict.pop(id)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_questions'))

if __name__ == '__main__':
    app.run(debug=True)
