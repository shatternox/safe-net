from flask import render_template, request, Blueprint, current_app, session
from safenet_app.dashboard.forms import LogForm
from safenet_app.models import Log
from safenet_app import db, app

dashboard = Blueprint('dashboard', __name__)


@dashboard.route("/dashboard", methods=['POST', 'GET'])
def dashboard():

    form = LogForm()
    data = ''
    time = ''
    log = ''

    if form.data.data:
        data = form.data.data
        print(data)
        time = form.time.data
        print(time)

        masukin = Log(time=time, log=data)

        db.session.add(masukin)
        db.session.commit()

        log = Log.query.all()
    log = Log.query.all()

    return render_template("dashboard.html", form=form, data=data, time=time, log=log)



