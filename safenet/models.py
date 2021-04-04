from safenet import db
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
import datetime

bcrypt = Bcrypt()


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

class Log(db.Model):

    __tablename__ = 'log'

    client_id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String, nullable=False)
    log = db.Column(db.String, nullable=False)

    def __init__(self, time, log):
        self.time = time
        self.log = log