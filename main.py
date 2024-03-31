# Main file pulls in mapping for the users who will be called as well as the controller mappings and image mappings.
# The program runs on a loop waiting for input from a button. When a button is pressed, the code responds based on what the button and what the screen looks like at the time.


from evdev import InputDevice, categorize, ecodes, list_devices
import button_controls, telegram_interact, text_to_speech, screen_controller
import time
from dotenv import load_dotenv
import os

device_name = "DragonRise Inc."
gamepad = InputDevice(button_controls.find_device_by_name(device_name).path)
button_mappings = button_controls.button_mappings
image_mappings = screen_controller.image_mappings

load_dotenv()
chat_id_mimi_papa = os.getenv("TELEGRAM_CHAT_MIMI_PAPA")
chat_id_aberash = os.getenv("TELEGRAM_CHAT_ABERASH")
chat_id_aubrey = os.getenv("TELEGRAM_CHAT_AUBREY")
chat_id_simret = os.getenv("TELEGRAM_CHAT_SIMRET")
api_key = os.getenv("TELEGRAM_API_KEY")

# print(api_key)

in_a_call_flag = False
incoming_call_flag = False
call_lockout = False

call_mapping = [
    [chat_id_mimi_papa, "Calling Mimi and Papa"],
    [chat_id_aberash, "Calling Mommy"],
    [chat_id_aubrey, "Calling Bob"],
    [chat_id_simret, "Calling Sissy"]
]

# handle buttons when requesting a call
def request_call(api_key, user_info):
    telegram_interact.send_message(api_key, user_info[0], user_info[1])

# main function for program
def main():
    for event in gamepad.read_loop():

        # check for button input
        if event.type == ecodes.EV_KEY:
            data = categorize(event)
            if data.keystate == 1:  # Button down
                button = button_mappings.get(data.scancode)

                if button:
                    # if the call button is available, click it
                    if button == '8':
                        button_location = screen_controller.check_for_button(image_mappings[1][1], image_mappings[1][2])

                        if button_location:
                            screen_controller.click_on_button(button_location)
                            time.sleep(3)

                            screen_controller.click_on_button(image_mappings[3][2], clicks=2)

                    elif button == '2':
                        request_call(api_key, call_mapping[0])
                    elif button == '3':
                        request_call(api_key, call_mapping[1])
                    elif button == '4': 
                        print(call_mapping)
                        request_call(api_key, call_mapping[2])
                    elif button == '5':
                        request_call(api_key, call_mapping[3])
                    elif button == '6':
                        pass
                    elif button == '7':
                        pass
                    # if hangup buttons are available, click on them
                    elif button == '1':
                        try:
                            button_location = screen_controller.check_for_button(image_mappings[0][1], image_mappings[0][2])

                            if button_location:
                                print("Clicking on button")
                                screen_controller.click_on_button(button_location)
                        except:
                            print("Not found")
                        
                        try:
                            button_location = screen_controller.check_for_button(image_mappings[2][1], image_mappings[2][2])

                            if button_location:
                                print("Clicking on button")
                                screen_controller.click_on_button(button_location)
                        except:
                            print("Not found")

if __name__ == "__main__":
    main()