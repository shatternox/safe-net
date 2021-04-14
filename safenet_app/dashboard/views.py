from flask import render_template, request, Blueprint, current_app, session
from safenet_app import app

dashboard = Blueprint('dashboard', __name__)

@dashboard.route("/dashboard", methods=['POST', 'GET'])
def dashboard():



    return render_template("dashboard.html", form=form)



