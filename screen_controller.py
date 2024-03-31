# check for call ui buttons (calling and in call variations)
# make buttons available when ui buttons appear
# when call is started make it full screen, check to make sure mute button is off, and camera button is on


import pyautogui
import time
import os


current_directory = os.getcwd()
pyautogui.useImageNotFoundException()
# center_of_screen = (450,900,180,105)

image_mappings = [
    ['call_deny_icon', '/home/hubble/dashboard-code/dashboard_call_interface/screenshots/decline_call_icon.png', (450, 1200, 180, 105)],
    ['call_accept_icon', '/home/hubble/dashboard-code/dashboard_call_interface/screenshots/incoming_call_icon.png', (450, 1200, 180, 105)],
    ['hangup_icon', '/home/hubble/dashboard-code/dashboard_call_interface/screenshots/decline_call_icon.png', (450,1810,180,105)],
    ['center_of_screen','',(450,900,180,105)]
]

# find an image on screen and click on the middle of it
def click_on_button(image_location, clicks=1):
    x, y = pyautogui.center(image_location)
    pyautogui.click(x, y, clicks)

# look for if a call is coming in.
def check_for_button(location, region):
    try:
        image = pyautogui.locateOnScreen(location, region=region, confidence=0.8)
        if image != None:
            take_screenshot(region)
            return image
    except pyautogui.ImageNotFoundException:
        return False

def take_screenshot(image_region):
    im1 = pyautogui.screenshot(region=image_region)
    im1.save(r"./savedimage.png")