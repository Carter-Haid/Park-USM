#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request, redirect
import pyrebase
import GetMap

app = Flask(__name__)

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


@app.route("/admin", methods=['GET', 'POST'])
def login():
    unsuccessful = 'Please check your credentials'
    successful = 'Login successful'
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('AdminControls.html', s=successful)
        except:
            return render_template('login.html', us=unsuccessful)

    return render_template('login.html')


@app.route('/')
def home():
    GetMap.getmap()
    return render_template('GorhamMap.html')


if __name__ == '__main__':
    app.run()


# In[ ]:
