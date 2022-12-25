from flask_wtf import FlaskForm
from wtforms import (
    widgets, StringField, SubmitField, EmailField,
    IntegerField, SelectField, SelectMultipleField, TextAreaField
)
from wtforms.validators import DataRequired

class SurveyForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    gender = SelectField('Гендер',coerce=str,
                            choices=[('женщина', 'женщина'), ('мужчина', 'мужчина'),
                                     ('другой', 'другой')
                                     ]
                            )
    education = SelectField('Образование',coerce=str,
                            choices=[('детский сад', 'детский сад'), ('9 классов школы', '9 классов школы'),
                                     ('11 классов школы', '11 классов школы'),
                                     ('среднее специальное', 'среднее специальное'),
                                     ('неоконченное высшее', 'неоконченное высшее'),
                                     ('бакалавриат / специалитет', 'бакалавриат / специалитет'),
                                     ('магистратура', 'магистратура'),
                                     ('аспирантура', 'аспирантура'),
                                     ('кандидат наук', 'кандидат наук'),
                                     ('доктор наук', 'доктор наук')
                                     ]
                            )
    q1 = SelectField('капибара',coerce=str,
                            choices=[('животное', 'животное'), ('Австралия', 'Австралия'),
                                     ('чилл', 'чилл')
                                     ]
                            )
    q2 = SelectField('бабочка',coerce=str,
                            choices=[('еда', 'еда'), ('красота', 'красота'),
                                     ('Наполеон', 'Наполеон')
                                     ]
                            )
    q3 = SelectField('жизнь',coerce=str,
                            choices=[('дедлайны', 'дедлайны'), ('смерть', 'смерть'),
                                     ('meh', 'meh')
                                     ]
                            )
    q4 = SelectField('лингвистика',coerce=str,
                            choices=[('смерть', 'смерть'), ('непотизм', 'непотизм'),
                                     ('радость', 'радость')
                                     ]
                            )
    q5 = SelectField('каникулы',coerce=str,
                            choices=[('прога', 'прога'), ('мандарины', 'мандарины'),
                                     ('отдых', 'отдых')
                                     ]
                            )
    submit = SubmitField('Сохранить')
