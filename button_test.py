from evdev import InputDevice, categorize, ecodes

# Replace /dev/input/eventX with the event number of your gamepad
gamepad = InputDevice('/dev/input/event6')

# Define the button mappings (replace with your own values)
button_mappings = {
    0: 'button1',
    1: 'button2',
    2: 'button3',
    3: 'button4',
    4: 'button5',
    5: 'button6',
    6: 'button7',
    7: 'button8',
    8: 'button9',
    9: 'button10',
    10: 'button11',
    11: 'button12'
}

# Loop indefinitely and print button events
for event in gamepad.read_loop():
    print(event)
    if event.type == ecodes.EV_KEY:
        data = categorize(event)
        if data.keystate == 1:  # Button down
            button = button_mappings.get(data.scancode)
            if button:
                print(f'Button {button} pressed')
