from flask import send_from_directory, Flask, flash,render_template,request, redirect, url_for, session
from Forms import CreateUserForm
from EditMovies import UpdateMoviesForm
from EditRooms import CreateRoomsForm
import shelve, RoomInfo, MovieInfo, HomeInfo
from werkzeug.utils import secure_filename
import os

path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Make directory if "uploads" folder not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'thisisasecret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#@app.route('/Movies')
#def movies():
#    staff_dict = {}
#    db = shelve.open('storage.db', 'r')
#    staff_dict = db['Staff']
#    db.close()

#    staff_list = []
#    for key in staff_dict:
#        staff = staff_dict.get(key)
#        staff_list.append(staff)

#    return render_template('movies.html', staff_list=staff_list)

@app.route('/filter')
def vmd_timestamp():
    return render_template('moviesfilter.html')

@app.route('/purchase')
def purchase():
    return render_template('moviesstaff.html')

#moviesstaff - retrieve page
#staff_list – The 'staff_list list' will be used in the Retrieve Users template
# to retrieve and display the details of all the user objects that
# were stored in the users_dict dictionary that was stored in shelve.
@app.route('/MoviesStaff')
def moviesstaff():
    movieinfo_dict = {}
    db = shelve.open('movieinfostorage.db', 'r')
    movieinfo_dict = db['MovieInfo']
    db.close()

    movieinfo_list = []
    for key in movieinfo_dict:
        movieinfo = movieinfo_dict.get(key)
        movieinfo_list.append(movieinfo)

    return render_template('moviesstaff.html', movieinfo_list=movieinfo_list)

#@app.route('/MoviesStaff')
#def moviesstaff():
#    movieinfo_dict = {}
#    db = shelve.open('movieinfostorage.db', 'r')
#    movieinfo_dict = db['MovieInfo']
#    db.close()

#    movieinfo_list = []
#    for key in movieinfo_dict:
#        movieinfo = movieinfo_dict.get(key)
#        movieinfo_list.append(movieinfo)

#    return render_template('moviesstaff.html', movieinfo_list=movieinfo_list)

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

    return render_template('chooseMovies.html', movieinfo_list=movieinfo_list)

#@app.route('/CreateMovies', methods=['GET', 'POST'])
#def upload_file():
#    if request.method == 'POST':
        # check if the post request has the file part
#        if 'file' not in request.files:
#            flash('No file part')
#            return redirect(request.url)
#            file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
#        if file.filename == '':
#            flash('No selected file')
#            return redirect(request.url)
#        if file and allowed_file(file.filename):
#            filename = secure_filename(file.filename)
#            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#           flash('File successfully uploaded')
#            return redirect (url_for('staffeditmovies',filename=filename))
#        else:
#            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
#            return redirect(request.url)

@app.route('/CreateMovies', methods=['GET', 'POST'])
def CreateMovies(): #(filename?)
    create_movieform = UpdateMoviesForm(request.form)
#    file_url = send_from_directory(app.config['UPLOAD_FOLDER'],filename)
    if request.method == 'POST' and create_movieform.validate():

        movieinfo_dict = {}
        db = shelve.open('movieinfostorage.db', 'c')

        try:
            movieinfo_dict = db['MovieInfo']
        except:
            print("Error in retrieving Staff from storage.db.")

        movieinfo = MovieInfo.MovieInfo(
#                                   create_movieform.movie_title.data,
                                    create_movieform.movie_name.data,
#                                   file_url,
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

        movieinfo_dict[movieinfo.get_movie_id()] = movieinfo
        db['MovieInfo'] = movieinfo_dict

        # Test codes
        movieinfo_dict = db['MovieInfo'] #Value of Staff Key in Storage
        movieinfo = movieinfo_dict[movieinfo.get_movie_id()] #value of Value of Staff Key in Storage
        print("was stored in storage.mb successfully with user_id ==", movieinfo.get_movie_id())

        db.close()
        return redirect(url_for('home'))
    return render_template('createMovie.html', form=create_movieform)

@app.route('/UpdateMovie/<int:id>/', methods=['GET', 'POST'])
def UpdateMovie(id):
    update_movieform = UpdateMoviesForm(request.form)
    if request.method == 'POST' and update_movieform.validate():
        movieinfo_dict = {}
        db = shelve.open('movieinfostorage.db', 'w')
        movieinfo_dict = db['MovieInfo']

        movie = movieinfo_dict.get(id)
#        movie.set_movietitle(update_movieform.movie_title.data)
        movie.set_moviename(update_movieform.movie_name.data)
#        movie.set_movie_image(update_movieform.movie_image.data)
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

        return redirect(url_for('moviesstaff'))

    else:
        movieinfo_dict = {}
        db = shelve.open('movieinfostorage.db', 'r')
        movieinfo_dict = db['MovieInfo']
        db.close()

        movie = movieinfo_dict.get(id)
#        update_movieform.movie_title.data = movie.get_movietitle()
        update_movieform.movie_name.data = movie.get_moviename()
#        update_movieform.movie_image.data = movie.get_movie_image()
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

#@app.route('/delete_user', methods=['POST'])
#def delete_movie():
#    staff_dict = {}
#    db = shelve.open('storage.db', 'w')
#    staff_dict = db['Staff']

#    staff_dict.pop()

#    db['Staff'] = staff_dict
#    db.close()

#    return redirect(url_for('moviesstaff.html'))

#@app.route('/Staff')
#def staff():
#    return render_template('testform.html')

if __name__ == '__main__':
    app.run(debug=True)
