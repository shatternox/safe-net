import os
import datetime
import pyrebase
from flask import Flask

config = {
    "apiKey": "AIzaSyDGFga2ngSMoFbi4oYM8oSuKnJ0kbK0I-I",
    "authDomain": "safe-net-2bee3.firebaseapp.com",
    "databaseURL": "https://safe-net-2bee3-default-rtdb.firebaseio.com",
    "projectId": "safe-net-2bee3",
    "storageBucket": "safe-net-2bee3.appspot.com",
    "messagingSenderId": "1087212813689",
    "appId": "1:1087212813689:web:a136ae0c50be6c5c2e03a8",
    "measurementId": "G-X3NKV36LGQ"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

'''
db = firebase.database()
db.child("users").push({
    "email": ""
    "password": ""
    })

db.child("users").update({"email":""})

users = db.child("users").push({
    "email": ""
    "password": ""
    })

print(users.val()) >> ordered dictionary

db.child("users").remove()


'''

app = Flask(__name__)

app.config['SECRET_KEY'] = "asdadadasa;dksa;ldks;ald;lasdka"


# db = SQLAlchemy(app)
# Migrate(app, db)

from safenet_app.core.views import core
app.register_blueprint(core)

# from safenet_app.dashboard.views import dashboard
# app.register_blueprint(dashboard)

from safenet_app.users.views import users
app.register_blueprint(users)

