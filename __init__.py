from flask import Flask,request,render_template,request, redirect, url_for, session
from Forms import CreateUserForm
from EditMovies import CreateMoviesForm
from EditRooms import CreateRoomsForm
import shelve, MoviesStaff

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

@app.route('/purchase')
def purchase():
    return render_template('moviesstaff.html')

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
