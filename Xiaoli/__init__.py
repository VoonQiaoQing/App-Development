import shelve
from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin
from Forms import LoginForm, RegisterForm
import imghdr
import os
from werkzeug.datastructures import CombinedMultiDict
from werkzeug.utils import secure_filename
from flask_uploads import configure_uploads, UploadSet, IMAGES

app = Flask(__name__)
app.secret_key = 'itSaSeCret'
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# photos = UploadSet('photos', IMAGES)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'profilepic')
# app.config['UPLOAD_EXTENSIONS'] = ['.jfif', '.webp', '.jpg', '.png', '.gif']
# configure_uploads(app, photos)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


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

    def get_id(self):
        return self.id

    def __repr__(self):
        return f'<CuUser: {self.username}>'


class staff:
    id = 0

    def __init__(self, username, gender, email, password):
        self.id = staff.id
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

    def get_id(self):
        return self.id

    def __repr__(self):
        return f'<CuUser: {self.username}>'


staffacc = staff('Golden123', 'Female', 'golden123@gmail.com', 'goldenmovie')
int(staffacc.get_id())


@login_manager.user_loader
def load_user(user_id):
    return CuUser.get_id(user_id)


@app.route('/')
def home():
    # session['loginInuser'] = "lookitfan@gmail.com"
    users_dict = {}
    db = shelve.open('users.db', 'w')
    users_dict = db['Users']
    db.close()
    user = users_dict.get(id)
    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)
    return render_template('home.html', user=user, staffacc=staffacc)


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


@app.route('/profile/<int:id>', methods=['GET', 'POST'])
def profile(id):
    update_form = RegisterForm(request.form)
    users_dict = {}
    db = shelve.open('users.db', 'r')
    users_dict = db['Users']
    db.close()

    user = users_dict.get(id)
    update_form.username.data = user.username
    update_form.email.data = user.email
    update_form.gender.data = user.gender

    return render_template('profile.html', form=update_form, user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        users_dict = {}
        db = shelve.open('users.db', 'r')
        users_dict = db['Users']
        db.close()
        users_list = []
        if login_form.email.data == staffacc.email:
            if staffacc.password == login_form.password.data:
                session['id'] = True
                session['login'] = staffacc.id
                session['loggedIn'] = staffacc.username
                return redirect(url_for('home'))
        else:
            for id in users_dict:
                user = users_dict.get(id)
                users_list.append(user)
            for user in users_list:
                if user.email == login_form.email.data:
                    password = generate_password_hash(login_form.password.data, method='sha256')
                    check_password_hash(user.password, password)
                    session['id'] = True
                    session['login'] = user.id
                    session['loggedIn'] = user.username
                    return redirect(url_for('home'))
    return render_template('login.html', form=login_form)

'''
@app.route('/', methods=['GET', 'POST'])
def upload():
    # room_form = CreateRoomsForm(CombinedMultiDict((request.files, request.form)))
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        if filename != '':
            file_ext1 = os.path.splitext(filename)[1]
            if file_ext1 not in app.config['UPLOAD_EXTENSIONS']:
                return "Invalid Image", 400
            else:
                filename.save(os.path.join(basedir, 'profilepic', filename))
                users_dict = {}
                db = shelve.open('users.db', 'r')
                users_dict = db['Users']
                user = users_dict.get(id)

            return redirect(url_for('home'))

    return render_template('update.html')


@app.route('/update/<filename>/')
def send_image(filename):
    return send_from_directory('profilepic', filename)


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

'''


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

        session['loggedIn'] = user.username
        return redirect(url_for('home'))

    else:
        users_dict = {}
        db = shelve.open('users.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_form.username.data = user.username
        update_form.email.data = user.email
        update_form.gender.data = user.gender

        return render_template('update.html', form=update_form, user=user, staffacc=staffacc)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):

    users_dict = {}
    db = shelve.open('users.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()
    session.pop('login')
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('login')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
