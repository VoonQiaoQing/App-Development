import shelve
from flask import Flask, render_template, request, redirect, url_for, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from Forms import LoginForm, RegisterForm
from flask_login import LoginManager, UserMixin


app = Flask(__name__)
app.secret_key = 'itSaSeCret'
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
                password = generate_password_hash(login_form.password.data, method='sha256')
                check_password_hash(user.password, password)
                session['id'] = True
                session['login'] = user.id
                session['loggedIn'] = user.username
                return redirect(url_for('home'))
    return render_template('login.html', form=login_form)


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
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('login')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
