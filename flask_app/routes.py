from flask_app import app, db
from flask import render_template, redirect
from flask_app.forms import SurveyForm
from flask_app.models import User, Answers
from sqlalchemy import func
import sqlite3

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/survey', methods=['POST', 'GET'])
def info():
    form = SurveyForm()
    if form.validate_on_submit():
        username = form.username.data
        gender = form.gender.data
        education = form.education.data
        age = form.age.data
        user = User(
            username=username,
            age=age,
            gender=gender,
            education=education
        )
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        db.session.commit()
        #print(cur.fetchall())
        new_survey = Answers(
            id=user.id,
            q1=form.q1.data,
            q2=form.q2.data,
            q3=form.q3.data,
            q4=form.q4.data,
            q5=form.q5.data
        )
        #print(id)
        db.session.add(new_survey)
        db.session.commit()
        return render_template('survey_done.html', form=form,
                              text='Ваша анкета:')
    return render_template('survey.html', form=form,
                          text='Ответьте на вопросы:')

@app.route('/stats')
def stats():
    # заводим словарь для значений (чтобы не передавать каждое в render_template)
    all_info = {}
    age_stats = db.session.query(
        func.avg(User.age),  # средний возраст AVG(user.age)
        func.min(User.age),  # минимальный возраст MIN(user.age)
        func.max(User.age)  # максимальный возраст MAX(user.age)
    ).one()  # берем один результат (он всего и будет один)
    def freq(que):
        freq = {}
        for one in que:
            if one[0] not in freq:
                freq[one[0]] = 1
            else:
                freq[one[0]] += 1
        [max_int, word] = [0, '']
        for one in freq:
            if freq[one] > max_int:
                [max_int, word] = [freq[one], one]
        return word
    freq_all = {}
    freq_all['q1'] = freq(db.session.query(Answers.q1).all())
    freq_all['q2'] = freq(db.session.query(Answers.q2).all())
    freq_all['q3'] = freq(db.session.query(Answers.q3).all())
    freq_all['q4'] = freq(db.session.query(Answers.q4).all())
    freq_all['q5'] = freq(db.session.query(Answers.q5).all())
    all_info['age_mean'] = age_stats[0]
    all_info['age_min'] = age_stats[1]
    all_info['age_max'] = age_stats[2]

    # это простой запрос, можно прямо у таблицы спросить
    all_info['total_count'] = User.query.count()  # SELECT COUNT(age) FROM user


    return render_template('results.html', all_info=all_info, freq_all=freq_all)

