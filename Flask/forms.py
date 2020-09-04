from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from flask import Flask, render_template
from flask_mail import Mail

import os





class SignupForm(FlaskForm):
    username = StringField('Имя пользователя', validators= [DataRequired()])
    phone = StringField('Телефон', validators=[NumberRange(min=9, max=16)])
    mail = StringField('E-mail', validators=[DataRequired()])
    body = StringField('Text', validators=[DataRequired()])
    submit = SubmitField('Войти')