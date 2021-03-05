#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pyrebase
from flask_compress import Compress
from flask import Flask, render_template, request, redirect, send_from_directory
from ModalVariableStyle import *
from contactForm import *
from PortlandMap import portlandmap


app = Flask(__name__,
            static_folder="static",
            template_folder="templates")
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
    exec(open("/home/carter/PycharmProjects/campusParkingMap/flaskr/banDetection.py").read())
    return render_template('index.html', gorhamopen=gorhamopen, portlandopen=portlandopen,
                           lewistonopen=lewistonopen, gorhamstreetstatus=gorhamstreetstatus,
                           portlandstreetstatus=portlandstreetstatus, lewistonstreetstatus=lewistonstreetstatus,
                           gorhambancounter=gorhammap(), portlandbancounter=portlandmap(),
                           usmgorhamicon=usmgorhamicon, usmportlandicon=usmportlandicon,
                           usmlewistonicon=usmlewistonicon,
                           gorhamstreeticon=gorhamstreeticon, portlandstreeticon=portlandstreeticon,
                           lewistonstreeticon=lewistonstreeticon, gorbancolor=gorbancolor,
                           porbancolor=porbancolor, usmgorcolor=usmgorcolor,
                           usmporcolor=usmporcolor, usmlewcolor=usmlewcolor,
                           gorcolor=gorcolor, porcolor=porcolor, lewcolor=lewcolor,
                           gorhamstreeticoncolor=gorhamstreeticoncolor, portlandstreeticoncolor=portlandstreeticoncolor,
                           lewistonstreeticoncolor=lewistonstreeticoncolor, usmlewistoniconcolor=usmlewistoniconcolor,
                           usmportlandiconcolor=usmportlandiconcolor, usmgorhamiconcolor=usmgorhamiconcolor,
                           pogobaninfo=pogobaninfo, lewbaninfo=lewbaninfo, gorhambaninfo=gorhambaninfo,
                           portlandbaninfo=portlandbaninfo, lewistonbaninfo=lewistonbaninfo)


@app.route('/portland')
def portland():
    exec(open("/home/carter/PycharmProjects/campusParkingMap/flaskr/banDetection.py").read())
    return render_template('portlandmap.html', gorhamopen=gorhamopen, portlandopen=portlandopen,
                           lewistonopen=lewistonopen, gorhamstreetstatus=gorhamstreetstatus,
                           portlandstreetstatus=portlandstreetstatus, lewistonstreetstatus=lewistonstreetstatus,
                           gorhambancounter=gorhammap(), portlandbancounter=portlandmap(),
                           usmgorhamicon=usmgorhamicon, usmportlandicon=usmportlandicon,
                           usmlewistonicon=usmlewistonicon,
                           gorhamstreeticon=gorhamstreeticon, portlandstreeticon=portlandstreeticon,
                           lewistonstreeticon=lewistonstreeticon, gorbancolor=gorbancolor,
                           porbancolor=porbancolor, usmgorcolor=usmgorcolor,
                           usmporcolor=usmporcolor, usmlewcolor=usmlewcolor,
                           gorcolor=gorcolor, porcolor=porcolor, lewcolor=lewcolor,
                           gorhamstreeticoncolor=gorhamstreeticoncolor, portlandstreeticoncolor=portlandstreeticoncolor,
                           lewistonstreeticoncolor=lewistonstreeticoncolor, usmlewistoniconcolor=usmlewistoniconcolor,
                           usmportlandiconcolor=usmportlandiconcolor, usmgorhamiconcolor=usmgorhamiconcolor,
                           pogobaninfo=pogobaninfo, lewbaninfo=lewbaninfo, gorhambaninfo=gorhambaninfo,
                           portlandbaninfo=portlandbaninfo, lewistonbaninfo=lewistonbaninfo)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        contactemail = request.form['contactemail']
        message = request.form['message']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        send_mail(text=firstname + ' ' + lastname + '\n' + contactemail + '\n' + message, subject="Contact Form",
                  to_email="campusparkingproject@gmail.com")
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


@app.route('/sw.js')
@app.route('/robots.txt')
@app.route('/manifest.json')
@app.route('/asset-manifest.json')
def static_files():
    return send_from_directory(app.static_folder, request.path[1:])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True)

# In[ ]:
