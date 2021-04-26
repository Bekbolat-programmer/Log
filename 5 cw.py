from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, redirect, render_template

ap = Flask(__name__)
ap.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    usid = StringField('Id астронавта', validators=[DataRequired()])
    ps = PasswordField('Пароль астронавта', validators=[DataRequired()])
    cpid = StringField('Id капитана', validators=[DataRequired()])
    ps2 = PasswordField('Пароль капитана', validators=[DataRequired()])
    sb = SubmitField('Доступ')


@ap.route('/login', methods=['GET', 'POST'])
def login():
    fr = LoginForm()
    if fr.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', fr=fr)


@ap.route('/')
def index():
    return redirect('/login')


@ap.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    ap.run(port=8080, host='127.0.0.1')