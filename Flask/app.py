from flask_mail import Mail, Message
import os
# import __init__

from flask import Flask, request, redirect, url_for, render_template, flash

app = Flask(__name__)



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
mail= Mail(app)



@app.route('/')
def hello_world():

    return render_template('body.html')

@app.route('/documents/1')
def body2():
    return render_template('body2.html')

@app.route('/documents/2')
def body2_2():
    return render_template('body2_2.html')

@app.route('/documents/3')
def body2_3():
    return render_template('body2_3.html')

@app.route('/documents/4')
def body2_4():
    return render_template('body2_4.html')
@app.route('/documents/5')
def body2_5():
    return render_template('body2_5.html')

@app.route('/documents/6')
def body2_6():
    return render_template('body2_6.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    username = request.form.get('username')

    phone = str(request.form.get('phone'))
    maill = request.form.get('mail')

    msg = Message(username, sender='0148965@gmail.com', recipients=[maill])
    msg.body = (phone)
    mail.send(msg)
    return render_template("body.html")

@app.errorhandler(500)
def pageNotFound(error):
    return render_template("505.html")
# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#
#       return render_template('result.html', result = result)



   # username = request.form.get('username')
   # phone = request.form.get('phone')
   # gmail = request.form.get('mail')
   # body = request.form.get('body')
   # bodyy = str(username+'_' + phone+'_' +'_' +body)
   # print(str(bodyy))




#
if __name__ == '__main__':
    app.run(host='0.0.0.0')


