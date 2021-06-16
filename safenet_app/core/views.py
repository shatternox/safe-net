from flask import render_template, request, Blueprint, current_app, session
from safenet_app.core.forms import ContactForm
import os
from safenet_app import auth

core = Blueprint('core', __name__)


@core.route("/")
@core.route("/index")
def index():

    current_user = session.get('usr');
    print(current_user)
    return render_template("index.html", title="Home", usr=current_user)


@core.route("/about")
def about():
    current_user = session.get('usr');
    print(current_user)
    return render_template("about.html", title="About", usr=current_user)


@core.route("/contact", methods=['GET','POST'])
def contact():
    form = ContactForm()
    if request.method == "POST":
        pass

        if form.validate_on_submit:
            pass
    return render_template("contact.html", title="Contact", form=form)



