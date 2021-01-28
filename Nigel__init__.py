from flask import Flask, render_template,request, redirect, url_for
from Forms import CreateUserForm
import shelve, User


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

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
    app.run()