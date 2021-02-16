from flask import Flask, render_template,request, redirect, url_for
from NigelForms import CreateQuestionForm

import shelve, User


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
@app.route("/get")



@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

@app.route('/createQuestion', methods=['GET', 'POST'])
def create_question():
    create_question_form = CreateQuestionForm(request.form)
    if request.method == 'POST' and create_question_form.validate():
        question_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            question_dict = db['Users']
        except:
            print("Error in retrieving Users from storage.db.")

        user = User.User(create_question_form.Question.data, create_question_form.Answer.data, create_question_form.Availability.data, create_question_form.NumberOfPeople.data, create_question_form.remarks.data)
        question_dict[user.get_user_id()] = user
        db['Users'] = question_dict
        db.close()



        return redirect(url_for('retrieve_questions'))
    return render_template('createQuestion.html', form=create_question_form)

@app.route('/retrieveQuestion')
def retrieve_questions():
    question_dict = {}
    db = shelve.open('storage.db', 'r')
    question_dict = db['Users']
    db.close()

    question_list = []
    for key in question_dict:
        user = question_dict.get(key)
        question_list.append(user)

    return render_template('retrieveQuestions.html',count=len(question_list), users_list=question_list)


@app.route('/updateQuestion/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_question_form = CreateQuestionForm(request.form)
    if request.method == 'POST' and update_question_form.validate():
        question_dict = {}
        db = shelve.open('storage.db', 'w')
        question_dict = db['Users']

        user = question_dict.get(id)
        user.set_Question(update_question_form.Question.data)
        user.set_Answer(update_question_form.Answer.data)
        user.set_Availability(update_question_form.Availability .data)
        user.set_NumberOfPeople(update_question_form.NumberOfPeople.data)
        user.set_remarks(update_question_form.remarks.data)

        db['Users'] = question_dict
        db.close()

        return redirect(url_for('retrieve_questions'))
    else:
        question_dict = {}
        db = shelve.open('storage.db', 'r')
        question_dict = db['Users']
        db.close()

        user = question_dict.get(id)
        update_question_form.Question.data = user.get_Question()
        update_question_form.Answer.data = user.get_Answer()
        update_question_form.Availability.data = user.get_Availability()
        update_question_form.NumberOfPeople.data = user.get_NumberOfPeople()
        update_question_form.remarks.data = user.get_remarks()

        return render_template('updateQuestions.html', form=update_question_form)

@app.route('/deleteQuestion/<int:id>', methods=['POST'])
def delete_question(id):
        question_dict = {}
        db = shelve.open('storage.db', 'w')
        question_dict = db['Users']

        question_dict.pop(id)

        db['Users'] = question_dict
        db.close()

        return redirect(url_for('retrieve_questions'))


if __name__ == '__main__':
    app.run()