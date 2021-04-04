from flask import render_template, request, Blueprint, current_app, session
from safenet import db
import os

core = Blueprint('core', __name__)


@core.route("/")
@core.route("/index")
@core.route("/login")
def index():
    return render_template("index.html")
