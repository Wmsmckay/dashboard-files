import keyboard

def on_press(key):
    print(key.name, key.scan_code)

keyboard.on_press(on_press)

# wait for keyboard events
keyboard.wait()