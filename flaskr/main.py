#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pyrebase
import ssl
from flask_compress import Compress
from flask import Flask, render_template, request, redirect, make_response, send_from_directory
from ModalVariableStyle import *
from flaskr.PortlandMap import portlandmap

app = Flask(__name__,
            static_folder="/home/carter/PycharmProjects/campusParkingMap/flaskr/static",
            template_folder="/home/carter/PycharmProjects/campusParkingMap/flaskr/templates")
Compress(app)

config = {
    "apiKey": "AIzaSyCXlNX11kHA9eXg_iGSfVrYniNLLNUF3nc",
    "authDomain": "campus-parking-project.firebaseapp.com",
    "databaseURL": "https://campus-parking-project.firebaseio.com",
    "projectId": "campus-parking-project",
    "storageBucket": "campus-parking-project.appspot.com",
    "messagingSenderId": "769852995231",
    "appId": "1:769852995231:web:2adea4edb9031518a594aa",
    "measurementId": "G-7R4TP4YTHX"}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        global email
        email = request.form['name']
        password = request.form['pass']
        try:
            global user
            user = auth.sign_in_with_email_and_password(email, password)
            return redirect('/admincontrols')
        except:
            return render_template('login.html')
    return render_template('login.html')


@app.route('/')
def home():
    gorhammap()
    return render_template('index.html', gorhamopen=gorhamcampus()[3], portlandopen=portlandcampus()[3],
                           lewistonopen=lewistoncampus()[3], gorhamstreetstatus=gorstreetbancolor()[2],
                           portlandstreetstatus=porstreetbancolor()[2], lewistonstreetstatus=lewstreetbancolor()[3],
                           gorhambancounter=gorhammap(), portlandbancounter=portlandmap(),
                           usmgorhamicon=gorhamcampus()[1], usmportlandicon=portlandcampus()[1],
                           usmlewistonicon=lewistoncampus()[1],
                           gorhamstreeticon=gorstreetbancolor()[0], portlandstreeticon=porstreetbancolor()[0],
                           lewistonstreeticon=lewstreetbancolor()[1], gorbancolor=gorbancolorfunction(),
                           porbancolor=porbancolorfunction(), usmgorcolor=gorhamcampus()[0],
                           usmporcolor=portlandcampus()[0], usmlewcolor=lewistoncampus()[0],
                           gorcolor=gorstreetbancolor()[3],
                           porcolor=porstreetbancolor()[3], lewcolor=lewstreetbancolor()[0],
                           gorhamstreeticoncolor=gorstreetbancolor()[1], portlandstreeticoncolor=porstreetbancolor()[1],
                           lewistonstreeticoncolor=lewstreetbancolor()[2], usmlewistoniconcolor=lewistoncampus()[2],
                           usmportlandiconcolor=portlandcampus()[2], usmgorhamiconcolor=gorhamcampus()[2])


@app.route('/portland')
def portland():
    portlandmap()
    return render_template('portlandmap.html', gorhamopen=gorhamcampus()[3], portlandopen=portlandcampus()[3],
                           lewistonopen=lewistoncampus()[3], gorhamstreetstatus=gorstreetbancolor()[2],
                           portlandstreetstatus=porstreetbancolor()[2], lewistonstreetstatus=lewstreetbancolor()[3],
                           gorhambancounter=gorhammap(), portlandbancounter=portlandmap(),
                           usmgorhamicon=gorhamcampus()[1], usmportlandicon=portlandcampus()[1],
                           usmlewistonicon=lewistoncampus()[1],
                           gorhamstreeticon=gorstreetbancolor()[0], portlandstreeticon=porstreetbancolor()[0],
                           lewistonstreeticon=lewstreetbancolor()[1], gorbancolor=gorbancolorfunction(),
                           porbancolor=porbancolorfunction(), usmgorcolor=gorhamcampus()[0],
                           usmporcolor=portlandcampus()[0], usmlewcolor=lewistoncampus()[0],
                           gorcolor=gorstreetbancolor()[3],
                           porcolor=porstreetbancolor()[3], lewcolor=lewstreetbancolor()[0],
                           gorhamstreeticoncolor=gorstreetbancolor()[1], portlandstreeticoncolor=porstreetbancolor()[1],
                           lewistonstreeticoncolor=lewstreetbancolor()[2], usmlewistoniconcolor=lewistoncampus()[2],
                           usmportlandiconcolor=portlandcampus()[2], usmgorhamiconcolor=gorhamcampus()[2])


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        contactemail = request.form['contactemail']
        try:
            print(firstname + " " + lastname + " " + contactemail)
        except:
            print("error")
    return render_template('contact.html')


@app.route('/passwordreset', methods=['GET', 'POST'])
def passwordreset():
    if request.method == 'POST':
        email = request.form['name']
        try:
            auth.send_password_reset_email(email)
        except:
            print("null")
    return render_template('forgotPassword.html')


@app.route('/admincontrols')
def admincontrols():
    return render_template('AdminControls.html', value=email)
    # TODO: Verify the user is logged in before rendering this page.


@app.route('/sw.js')
def sw():
    return app.send_static_file('sw.js')


@app.route('/asset-manifest.json')
def manifest():
    response = make_response(
                     send_from_directory('static', filename='asset-manifest.json'))
    return response


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, threaded=True)

# In[ ]:
