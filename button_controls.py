import time
from text_to_speech import speak
import os
from evdev import InputDevice, categorize, ecodes, list_devices

# Define button mappings here
button_mappings = {
    ecodes.BTN_BASE2: '1',
    ecodes.BTN_PINKIE: '2',
    ecodes.BTN_BASE: '3',
    ecodes.BTN_TOP2: '4',
    ecodes.BTN_TOP: '5',
    ecodes.BTN_THUMB2: '6',
    ecodes.BTN_THUMB: '7',
    ecodes.BTN_TRIGGER: '8',
}



def find_device_by_name(device_name):
    devices = [InputDevice(path) for path in list_devices()]
    for device in devices:
        if device_name in device.name:
            # print(device.name)
            # print(device.path)
            return device
    return None   


# device_name = "DragonRise Inc."
# gamepad = InputDevice(find_device_by_name(device_name).path)



# button = button_mappings.get(data.scancode)

# if data.keystate == 1:  # Button down

# def wait_for_second_press(button, timeout=3):
#     start_time = time.monotonic()
#     while time.monotonic() - start_time < timeout:
#         try:
#             event = gamepad.read_one()
#         except BlockingIOError:
#             event = None
#         if event is not None:
#             if event.type == ecodes.EV_KEY:
#                 data = categorize(event)
#                 if data.keystate == 1 and button_mappings.get(data.scancode) == button:
#                     # print(f'Button {button} pressed again within {timeout} seconds')
#                     return True
#     # print(f'Button {button} not pressed again within {timeout} seconds')
#     return False

# def handle_button_input(strButton):
#     button = int(strButton)
#     speak(f"Do you want to call {participants[button-1]['name']}?")