from flask_app import db


class User(db.Model):
    __tablename__ = 'user'  # имя таблицы
    username = db.Column(db.String(10))
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    education = db.Column(db.String(200))
    def __repr__(self):
        return '<User {}>'.format(self.username)
class Answers(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Text, primary_key=True)
    q1 = db.Column(db.Text)
    q2 = db.Column(db.Text)
    q3 = db.Column(db.Text)
    q4 = db.Column(db.Text)
    q5 = db.Column(db.Text)
