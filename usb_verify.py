from evdev import InputDevice, categorize, ecodes

# Define button mappings here
button_mappings = {
    ecodes.BTN_TRIGGER: '1',
    ecodes.BTN_THUMB: '2',
    ecodes.BTN_THUMB2: '3',
    ecodes.BTN_TOP: '4',
    ecodes.BTN_TOP2: '5',
    ecodes.BTN_PINKIE: '7',
    ecodes.BTN_BASE: '6',
    ecodes.BTN_BASE2: '8',
}

# Find gamepad device
gamepad = None
devices = [InputDevice('/dev/input/event6')]
gamepad = devices[0]

# Loop indefinitely and print button events
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        data = categorize(event)
        if data.keystate == 1:  # Button down
            button = button_mappings.get(data.scancode)
            if button:
                print(f'Button {button} pressed')