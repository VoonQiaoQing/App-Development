import User
import shelve

from flask import Flask, render_template, request, redirect, url_for

from Forms import CreateUserForm

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/createReview', methods=['GET', 'POST'])
def create_review():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print('Error in retrieving Users from storage.db.')

        user = User.User(create_user_form.rating.data, create_user_form.review.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        # Test codes
        users_dict = db['Users']
        user = users_dict[user.get_user_id()]
        print(user.get_rating(), user.get_review(), 'was stored in storage.db successfully with user_id ==', user.get_user_id())
        db.close()

        return redirect(url_for('retrieve_reviews'))
    return render_template('CreateReview.html', form=create_user_form)


@app.route('/retrieveReviews')
def retrieve_reviews():
    users_dict = {}
    db = shelve.open('storage.db, 'r'')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

        return render_template('RetrieveReviews.html', count=len(users_list), users_list=users_list)


@app.route('/updateReview/<int:id>/', methods=['GET', 'POST'])
def update_review(id):
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('storage.db', 'w')
        users_dict = db('Users')

        user = users_dict.get(id)
        user.set_rating(update_user_form.rating.data)
        user.set_review(update_user_form.review.data)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_reviews'))
    else:
        users_dict = {}
        db = shelve.open('storage.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.rating.data = user.get_rating()
        update_user_form.reason.data = user.get_review()

        return render_template('updateReviews.html', form=update_user_form)


if __name__ == '__main__':
    app.run()
