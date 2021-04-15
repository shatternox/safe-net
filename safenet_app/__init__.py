import os
import datetime
import pyrebase
from flask import Flask

firebase_config = {
    "apiKey": "AIzaSyDGFga2ngSMoFbi4oYM8oSuKnJ0kbK0I-I",
    "authDomain": "safe-net-2bee3.firebaseapp.com",
    "databaseURL": "https://safe-net-2bee3-default-rtdb.firebaseio.com",
    "projectId": "safe-net-2bee3",
    "storageBucket": "safe-net-2bee3.appspot.com",
    "messagingSenderId": "1087212813689",
    "appId": "1:1087212813689:web:a136ae0c50be6c5c2e03a8",
    "measurementId": "G-X3NKV36LGQ"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__)

app.config['SECRET_KEY'] = "970009e57d5e078a5d89ec3df97b55445dd73b0daf402eccc00148d126236e87"


# db = SQLAlchemy(app)
# Migrate(app, db)

from safenet_app.core.views import core
app.register_blueprint(core)

from safenet_app.users.views import users
app.register_blueprint(users)

from safenet_app.administration.views import administration
app.register_blueprint(administration)

from safenet_app.error.error_handler import error_pages
app.register_blueprint(error_pages)

