# Video Call Dashboard
This code is designed to run on a computer with a peripherals connected to make use video calling with just touching a few buttons. It has controls for 8 arcade buttons and has a camera and display attached to it. It also has [Telegram](https://telegram.org/) installed and logged in to allow for the video calls.

## How it works
To make the dashboard simple, some compromises has to be made. It cannot make any calls from the arcade buttons and it cannot send unique messages. The way it works is after pushing one of the call buttons, a message is sent to a group chat with my own telegram account, the account of the person I want to reach, and a telegram bot. The message requests a call from the recipient. The user can then make a video call to the main user's account and it will display on the dashboard. Using the arcade buttons, the user can then accept or deny the call. Once in the call, the screen goes full screen, making it easier to see the recipient. The user can also press the deny button to hang up in th call. 

To control the screen I am using pyautogui. This was my solution because I couldn't find any SKD or CLI tools that would allow me to make and take video calls programmatically. I already had some familiarity with the python library for telegram so I ended up going with that. It also had really good video quality between mobile devices and the linux desktop machine.

## Know issues
Because I decided to go with Ubuntu for my linux distro, every time a screenshot is taken the screen flashes. This is hard coded into the gnome desktop and so I would have to recompile it to change it. I'd rather not do this so I'll just leave it for now. Pyautogui take a screenshot in order to look at what is on the screen for image recognition and so every time the answer and hang up buttons are pressed it flashes.