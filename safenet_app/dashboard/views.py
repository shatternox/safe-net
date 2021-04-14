from flask import render_template, request, Blueprint, current_app, session
from safenet_app import app

administration = Blueprint('administration', __name__)

@administration.route("/dashboard", methods=['POST', 'GET'])
def dashboard():

    return render_template("dashboard.html", form=form)



