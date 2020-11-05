from pyautogui import screenshot
from datetime import datetime

def get_screen_shot(format_picture="jpg"):
    time_now = str(datetime.now())
    name_file = time_now[0:10] + "-" + time_now[11:13] + "-" +time_now[14:16] +"." + format_picture
    try:
        screenshot(imageFilename=name_file)
    except:
        print("Error")