#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request, redirect
from flaskr.GorhamMap import gorhammap
from flaskr.PortlandMap import portlandmap
import pyrebase


app = Flask(__name__,
            static_folder="/home/carter/PycharmProjects/campusParkingMap/flaskr/static",
            template_folder="/home/carter/PycharmProjects/campusParkingMap/flaskr/templates")

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
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
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
    return render_template('index.html')


@app.route('/portland')
def portland():
    portlandmap()
    return render_template('portlandmap.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
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
    test = auth.get_account_info(user['idToken'])
    print(test)
    return render_template('AdminControls.html')
    # TODO: Verify the user is logged in before rendering this page.


if __name__ == '__main__':
    app.run()

# In[ ]:
