from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0')

