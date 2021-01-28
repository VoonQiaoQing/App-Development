import shelve, payment, booking
from flask import Flask, render_template, request, redirect, url_for, session
from EditMovies import CreateMoviesForm
from EditRooms import CreateRoomsForm
from Forms import Purchase
from Forms import Add_location
from Forms import Add_time
from checkoutform import Checkout
import rooms as rooms
import roomLoactionCapacity as room
import movieinfo as movieinfo
import admin as admin

app = Flask(__name__)

@app.route('/')
def home():
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
        db = shelve.open('admin_location.db', 'c')
        try:
            admin_location_dict = db['Location']
        except:
            print('Error in retrieving form from admin_location.db')

        add_location = admin.Add_location(add_location_form.location1.data, add_location_form.location2.data,  add_location_form.location3.data, add_location_form.location4.data, add_location_form.location5.data)
        add_location_dict[add_location.get_add_location_Id()] = add_location
        db['Location'] = add_location_dict
        db.close()
        return redirect(url_for('home'))
    return render_template('admin_location.html',form=add_location_form)
@app.route('/retrieve_location')
def retrieve_location():
    add_location_dict = {}
    db = shelve.open('admin_location.db','r' )
    admin_location_dict = db['Location']
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
        db = shelve.open('admin_location.db', 'w')
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
        db = shelve.open('location.db', 'r')
        location_dict = db['Location']
        db.close()

        location = location_dict.get(id)
        update_location_form.location1.data = location.get_location1()
        update_location_form.location2.data = location.get_location2()
        update_location_form.location3.data = location.get_location3()
        update_location_form.location4.data = location.get_location4()
        update_location_form.location5.data = location.get_location5()
        return render_template('updateLocation.html', form=update_location_form)

@app.route('/deletelocation/<int:id>', methods=['POST'])
def delete_location(id):
    location_dict = {}
    db = shelve.open('admin_location.db', 'w')
    location_dict = db['Location']

    location_dict.pop(id)

    db['Location'] = location_dict
    db.close()
#Time
@app.route('/add_time', methods=['GET', 'POST'])
def admin_time():
    add_time_form = Add_time(request.form)
    if request.method == 'POST' and add_time_form.validate():
        add_time_dict = {}
        db = shelve.open('admin_time.db', 'c')
        try:
            add_time_dict = db['Time']
        except:
            print('Error in retrieving form from admin_time.db')

        add_time = admin.Add_time(add_time_form.time1.data, add_time_form.time2.data,add_time_form.time3.data,add_time_form.time4.data,add_time_form.time5.data)
        add_time_dict[add_time.get_add_time_id()] = add_time
        db['Time'] = add_time_dict
        db.close()
        return redirect(url_for('home'))
    return render_template('admin_time.html',form=add_time_form)
@app.route('/retrieve_time')
def retrieve_time():
    admin_time_dict = {}
    db = shelve.open('admin_time.db','r' )
    admin_time_dict = db['Time']
    db.close()
    admin_time_list = []
    for key in admin_time_dict:
        admin = admin_time_dict.get(key)
        admin_time_list.append(admin)
    return render_template('retrieve_time.html', count=len(admin_time_list), admin_location_list=admin_time_list)
@app.route('/updatetime/<int:id>/', methods=['GET', 'POST'])
def updatetime(id):
    update_time_form = Add_time(request.form)
    if request.method == 'POST' and update_time_form.validate():
        time_dict = {}
        db = shelve.open('admin_time.db', 'w')
        time_dict = db['Time']
        time = time_dict.get(id)
        time.set_location1(update_time_form.time1.data)
        time.set_location2(update_time_form.time2.data)
        time.set_location3(update_time_form.time3.data)
        time.set_location4(update_time_form.time4.data)
        time.set_location5(update_time_form.time5.data)
        db['Time'] = time_dict
        db.close()
        return redirect(url_for('retrieve_time'))
    else:
        time_dict = {}
        db = shelve.open('time.db', 'r')
        time_dict = db['Time']
        db.close()

        time = time_dict.get(id)
        update_time_form.time1.data = time.get_time1()
        update_time_form.time2.data = time.get_time2()
        update_time_form.time3.data = time.get_time3()
        update_time_form.time4.data = time.get_time4()
        update_time_form.time5.data = time.get_time5()
        return render_template('updateTime.html', form=update_time_form)

# @app.route('/deletetime/<int:id>', methods=['POST'])
# def delete_time():





@app.route('/purchase/<int:id>/', methods=['GET', 'POST'])
def purchase(id):
    global movie, moviename
    if id == 1:
        movie = movieinfo.MovieInfo("{{ url_for('static', filename='demonslayer.webp') }}",'Demon Slayer', 'PG13: Some Coarese Language','116mins' )
        moviename = movie.get_moviename()
    elif id == 2:
        movie = movieinfo.MovieInfo("{{ url_for('static', filename='samjincompany.webp') }}",'Samjin Company English Class',
                                    'PG13: Some Coarese Language','110 mins' )
        moviename = movie.get_moviename()
    elif id ==3:
        movie = movieinfo.MovieInfo( "{{ url_for('static', filename='horizonline.webp') }}",'Horizon Line', 'NC16: Some Drug scenes','92mins' )
        moviename = movie.get_moviename()
    elif id ==4:
        movie = movieinfo.MovieInfo("{{ url_for('static', filename='thewitches.webp') }}",'The Witches', 'PG13: Some  Frightening Scenes','105mins')
        moviename = movie.get_moviename()
    elif id == 5:
            movie = movieinfo.MovieInfo("{{ url_for('static', filename='voiceofsilence.webp') }}",'Voice of silence', 'PG13: Some Violence','100mins' )
            movie = movie.get_moviename()
    elif id ==6:
        movie = movieinfo.MovieInfo("{{ url_for('static', filename='honestthief.webp') }}",'Honest Thief', 'PG13: Violence & Brief Coarse','99mins' )
        movie = movie.get_moviename()
    elif id ==7:
        movie = movieinfo.MovieInfo("{{ url_for('static', filename='kutuk.webp') }}",'Kutuk', 'NC16:Violence & Horror','83mins' )
        moviename = movie.get_moviename()
    elif id ==8:
        movie = movieinfo.MovieInfo("{{ url_for('static', filename='onward.webp') }}",'Disney/Pixar\'s Onwardr', '\'Need Rating\'','102mins' )
        moviename = movie.get_moviename()
    elif id == 9:
        movie = movieinfo.MovieInfo("{{ url_for('static', filename='21bridges.webp') }}",'21 Bridges', '(NC16: Coarse Language & Violence)','99mins' )
        moviename = movie.get_moviename()
    elif id ==  10:
        movie = movieinfo.MovieInfo("{{ url_for('static', filename='pinocchio.webp') }}",'Pinocchio', '(PG: Some Frightening Scenes)','125mins' )
        moviename = movie.get_moviename()
    elif id == 11:
        movie = movieinfo.MovieInfo("{{ url_for('static', filename='youreyestell.webp') }}",'Your Eyes Tell', '(PG13: Some Violence)','123mins' )
        moviename = movie.get_moviename()
    elif id ==12:
        movie = movieinfo.MovieInfo("{{ url_for('static', filename='thewidow.webp') }}",'The widow', '(NC16: Some Nudity & Disturbing Scenes)','86 mins' )
        moviename = movie.get_moviename()
    purchase_form = Purchase(request.form)
    admin_location_dict = {}
    location = shelve.open('admin_location.db', 'r')
    admin_location_dict = location['Location']
    location.close()
    admin_location_list = []
    for key in admin_location_dict:
        admin = admin_location_dict.get(key)
        admin_location_list.append(admin)
    for location in admin_location_list:
        purchase_form.location.choices = [location.get_location1(),location.get_location2(),location.get_location3(),location.get_location4(),location.get_location5()]

    db = shelve.open('admin_time.db','r' )
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
        db = shelve.open('purchase.db', 'c')
        try:
            purchase_dict = db['Purchase']
        except:
            print("Error in retrieving form from purchase.db.")

        purchase = booking.Booking(moviename,purchase_form.Date.data,purchase_form.Time.data, purchase_form.location.data,purchase_form.roomtype.data)
        purchase_dict[purchase.get_customerid()] = purchase
        db['Purchase'] = purchase_dict
        db.close()

        return redirect(url_for('checkout'))
    return render_template('purchase.html', form=purchase_form, movie=movie)
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    purchase_dict = {}
    db = shelve.open('purchase.db', 'r')
    purchase_dict = db['Purchase']
    db.close()

    purchase_list = []
    for key in purchase_dict:
        purchase = purchase_dict.get(key)
        purchase_list.append(purchase)
    checkout_form = Checkout(request.form)
    if request.method == 'POST' and checkout_form.validate():
        checkout_dict = {}
        db = shelve.open('checkout.db', 'c')
        try:
            checkout_dict = db['Checkout']
        except:
            print("Error in retrieving form from checkout.db .")
        checkout = payment.Payment(checkout_form.card_number1.data,checkout_form.card_number2.data,checkout_form.card_number3.data,checkout_form.card_number4.data,checkout_form.name_on_card.data,
                                   checkout_form.expiry_month.data, checkout_form.expiry_year.data,
                                   checkout_form.cvv_number.data)
        checkout_dict[checkout.get_customerid()] = checkout
        db['Checkout'] = checkout_dict
        db.close()
        return redirect(url_for('ticket'))
    return render_template('checkout.html', count=len(purchase_list), purchase_list=purchase_list, form=checkout_form)


@app.route('/ticket')
def ticket():
    purchase_dict = {}
    db = shelve.open('purchase.db','r' )
    purchase_dict = db['Purchase']
    db.close()
    purchase_list = []
    for key in purchase_dict:
        ticket = purchase_dict.get(key)
        purchase_list.append(ticket)
    return render_template('Tickets.html', count=len(purchase_list), purchase_list=purchase_list)


@app.route('/MoviesStaff')
def moviesstaff():
    return render_template('moviesstaff.html')


@app.route('/staffeditrooms', methods=['GET', 'POST'])
def staffeditrooms():
    create_staff_roomform = CreateRoomsForm(request.form)
    if request.method == 'POST' and create_staff_roomform.validate():

        staff_dict = {}
        db = shelve.open('storage.db', 'w')
        db['Staff'] = staff_dict

        #        staff = MoviesStaff.MoviesStaff(create_staff_roomform.room_title.data,
        #                                        create_staff_roomform.small_roominfo.data,
        #                                        create_staff_roomform.med_roominfo.data,
        #                                        create_staff_roomform.large_roominfo.data,
        #                                        )

        staff = staff_dict.get(id)
        staff.set_roomtitle(create_staff_roomform.room_title.data)
        staff.set_small_roominfo(create_staff_roomform.small_roominfo.data)
        staff.set_med_roominfo(create_staff_roomform.med_roominfo.data)
        staff.set_large_roominfo(create_staff_roomform.large_roominfo.data)

        #        staff_dict[staff.get_staff_id()] = staff
        db['Staff'] = staff_dict

        # Test codes
        #        staff_dict = db['Staff']
        #        staff = staff_dict[staff.get_staff_id()]
        #        print("was stored in storage.db successfully with user_id ==", staff.get_user_id())

        db.close()

        return redirect(url_for('home'))
    else:
        staff_dict = {}
        db = shelve.open('storage.db', 'r')
        db['Staff'] = staff_dict
        db.close()

        staff = staff_dict.get(id)
        create_staff_roomform.room_title.data = staff.get_roomtitle()
        create_staff_roomform.small_roominfo.data = staff.get_small_roominfo()
        create_staff_roomform.med_roominfo.data = staff.get_med_roominfo()
        create_staff_roomform.large_roominfo.data = staff.get_large_roominfo()

        staff_list = []
        for key in staff_dict:
            staff = staff_dict.get(key)
            staff_list.append(staff)

        return render_template('editRooms.html', form=create_staff_roomform, staff_list=staff_list)


@app.route('/staffeditmovies', methods=['GET', 'POST'])
def staffeditmovies():
    create_user_form2 = CreateMoviesForm(request.form)
    if request.method == 'POST' and create_user_form2.validate():
        return redirect(url_for('home'))
    return render_template('editMovies.html', form=create_user_form2)


@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')


@app.route('/Staff')
def staff():
    return render_template('testform.html')


if __name__ == '__main__':
    app.run(debug=True)
