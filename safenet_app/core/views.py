from flask import render_template, request, Blueprint, current_app, session
from safenet_app.core.forms import ContactForm
import os

core = Blueprint('core', __name__)


@core.route("/")
@core.route("/index")
def index():

    return render_template("index.html", title="Home")


@core.route("/about")
def about():

    return render_template("about.html", title="About")


@core.route("/contact", methods=['GET','POST'])
def contact():
    form = ContactForm()
    if request.method == "POST":
        pass

        if form.validate_on_submit:
            pass
    return render_template("contact.html", title="Contact", form=form)



