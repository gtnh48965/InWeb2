from flask import Flask, render_template
from flask_mail import Mail, Message
from forms import SignupForm
import os


app = Flask(__name__)
mail= Mail(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '0148965@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = '0148965@gmail.com'
app.config['MAIL_PASSWORD'] = 'Petr2028!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/result")
def index():

   msg = Message('Hello', sender = '0148965@gmail.com', recipients = ['gtnh48965@bk.ru'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return render_template("body.html")
      # jsonify(data)


