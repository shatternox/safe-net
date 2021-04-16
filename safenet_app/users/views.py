from flask import render_template, redirect, request, Blueprint, current_app, flash, url_for
from flask_login import login_user, current_user, logout_user, login_required
from safenet_app.users.forms import RegistrationForm, LoginForm
from safenet_app import auth, db


users = Blueprint('users', __name__)


@users.route("/logout")
def logout():

    try:
        auth.signOut()
    except:
        flash("Something wrong happened. Please try again")

    return redirect(url_for("core.index"))


@users.route("/register", methods=['GET','POST'])
def register():
    
    form = RegistrationForm()

    if request.method == 'POST':
        print(form.validate_on_submit())
        if form.validate_on_submit():

            user = auth.create_user_with_email_and_password(form.email.data, form.password.data)
            auth.send_email_verification(user['idToken'])

            flash("An verification has been send to your email. Please verify to login!")
            return redirect(url_for('users.login'))
    
    return render_template('register.html', form=form, title='Register')


@users.route("/login", methods=['GET','POST'])
def login():

    form = LoginForm()

    if request.method == 'POST':

        if form.validate_on_submit():

            user = auth.sign_in_with_email_and_password(form.email.data, form.password.data)
            
            return redirect(url_for("administration.dashboard"))

    return render_template('login.html', form=form, title='Login')
