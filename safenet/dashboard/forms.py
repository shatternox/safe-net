from flask_wtf import FlaskForm
from wtforms import StringField


class LogForm(FlaskForm):
    time = StringField('Time')
    data = StringField('Data')
