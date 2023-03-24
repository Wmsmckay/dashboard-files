import smtplib
import imaplib
import email
import json
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from evdev import InputDevice, categorize, ecodes
from gtts import gTTS


# Diver location
driver_location = '/usr/bin/chromedriver'

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

# dictionary of carrier email domains
carrier_domains = {
    'verizon': 'vtext.com',
    'att': 'txt.att.net',
    'sprint': 'messaging.sprintpcs.com',
    'tmobile': 'tmomail.net'
}

# email configuration
email_address = 'wms.dashboard01@gmail.com'
email_password = 'knodnonboophsvoz'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
imap_server = 'imap.gmail.com'
imap_port = 993

def speak(message):
    pass
    # Language in which you want to convert
    language = 'en'
    message = "." + message
    myobj = gTTS(text=message, lang=language, slow=False)
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("welcome.mp3")
    # Playing the converted file
    os.system("mpg321 welcome.mp3")

# function to send text message
def send_text_message(person):
    speak(f"Calling {person['name']}. Please wait to connect")

    phone_number=str(person['number'])
    carrier=str(person['carrier'])

    # sys.exit()
    # phone_number='3852410787'
    # carrier='verizon'
    message='Ladd and Selassie want to Facetime! Reply to this message with a Facetime link from the Facetime App. Or, reply with BUSY.'

    # construct email message
    to_email = f"{phone_number}@{carrier_domains[carrier]}"
    subject = ''
    body = message
    email_message = f"From: {email_address}\nTo: {to_email}\nSubject: {subject}\n\n{body}"

    # send email message
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, email_password)
    server.sendmail(email_address, to_email, email_message)
    server.quit()


def open_browser(message_url):
    speak("Connecting to Facetime")
    options = webdriver.ChromeOptions()
    #options.binary_location = binary_location
    options.add_argument(r'--use-fake-ui-for-media-stream') #e.g. Profile 3

    # set up the webdriver
    browser = webdriver.Chrome(executable_path=driver_location, options=options)

    browser.get(message_url) 
    # find the input field by its ID and enter "Ladd and Selassie"
    input_field = browser.find_element_by_id("name-entry")
    input_field.clear()
    input_field.send_keys("Ladd and Selassie")

    # click the "Continue" button
    continue_button = browser.find_element_by_xpath("//ui-button[@aria-label='Continue']")
    continue_button.click()

    # wait for the page to load
    time.sleep(3)

    try:
        # allow access to microphone and camera
        microphone = browser.find_element_by_xpath('//div[@class="permission-checkbox mic"]')
        microphone.click()
        camera = browser.find_element_by_xpath('//div[@class="permission-checkbox cam"]')
        camera.click()
    except:
        print("not there")

    try:
        speak("Joining call")
        # click the "Join" button by its ID
        join_button = browser.find_element_by_id("callcontrols-join-button-session-banner")
        join_button.click()

        # wait for the page to load
        time.sleep(2)

        # click the fullscreen button
        fullscreen_button = browser.find_element_by_css_selector('#callcontrols-fullscreen-button')
        fullscreen_button.click()

        # # close the browser window
        # browser.close()
    except:
        print("error with browser")



# def check_for_text_message_response():
#     try:
#         # login to IMAP server
#         mail = imaplib.IMAP4_SSL(imap_server, imap_port)
#         mail.login(email_address, email_password)
#         mail.select("inbox")
#         # search for unread messages
#         result, data = mail.search(None, "UNSEEN")
#         # loop through messages
#         for num in data[0].split():
#             result, data = mail.fetch(num, "(RFC822)")
#             email_message = email.message_from_bytes(data[0][1])

#             # loop through attachments
#             for part in email_message.walk():
#                 # check if attachment is a text file
#                 if part.get_content_type() == 'text/plain':
#                     filename = part.get_filename()
#                     # check if attachment has .txt extension
#                     # check if message has attachments
#                     if email_message.get_content_maintype() == 'multipart':
#                         for part in email_message.walk():
#                             # check if part is an attachment
#                             if part.get_content_disposition() is not None:
#                                 attachment = part.get_payload(decode=True)
#                                 # check if attachment exists and has a .txt extension
#                                 if attachment and filename and filename.endswith('.txt'):
#                                     # print contents of attachment
#                                     print(f"Contents of {filename}:")
#                                     print(attachment.decode())
#                                     # check if attachment contains a facetime url
#                                     if 'facetime.apple.com' in attachment.decode():
#                                         # print('its true!')
#                                         open_browser(attachment.decode())
#                                     # else:
#                                     #     for participant in participants:
#                                     #         if participant['number'] in email_message['From']:
#                                     #             name = participant['name']
#                                     #             speak(f"Sorry, {name} is not available right now.")
#                                     #     print(f"Phone number in email message: {email_message['From']}")

#             # mark message as read
#             mail.store(num, '+FLAGS', '\\Seen')

#         mail.close()
#         mail.logout()
#     except:
#         print("error checking messages")

def mark_all_emails_as_read():
    # login to IMAP server
    mail = imaplib.IMAP4_SSL(imap_server, imap_port)
    mail.login(email_address, email_password)
    mail.select("inbox")

    # search for unread messages
    result, data = mail.search(None, "UNSEEN")
    # loop through messages and mark as read
    for num in data[0].split():
        mail.store(num, '+FLAGS', '\\Seen')

    mail.close()
    mail.logout()

def check_for_text_message_response():
    # login to IMAP server
    mail = imaplib.IMAP4_SSL(imap_server, imap_port)
    mail.login(email_address, email_password)
    mail.select("inbox")

    # search for unread messages
    result, data = mail.search(None, "UNSEEN")
    # loop through messages
    for num in data[0].split():
        result, data = mail.fetch(num, "(RFC822)")
        email_message = email.message_from_bytes(data[0][1])

        # loop through attachments
        for part in email_message.walk():
            # check if attachment is a text file
            if part.get_content_type() == 'text/plain':
                filename = part.get_filename()
                # check if attachment has .txt extension
                # check if message has attachments
                if email_message.get_content_maintype() == 'multipart':
                    for part in email_message.walk():
                        # check if part is an attachment
                        if part.get_content_disposition() is not None:
                            attachment = part.get_payload(decode=True)
                            # check if attachment exists and has a .txt extension
                            if attachment and filename and filename.endswith('.txt'):
                                # print contents of attachment
                                print(f"Contents of {filename}:")
                                print(attachment.decode())
                                # check if attachment contains a facetime url
                                if 'facetime.apple.com' in attachment.decode():
                                    # print('its true!')
                                    open_browser(attachment.decode())
                                    # webbrowser.open_new_tab(attachment.decode())

        # mark message as read
        mail.store(num, '+FLAGS', '\\Seen')

    mail.close()
    mail.logout()




# Find gamepad device
gamepad = None
devices = [InputDevice('/dev/input/event6')]
gamepad = devices[0]

# print(gamepad)

# Load the data.
f = open("callers.json")
data = json.load(f)
participants = data["people"]

mark_all_emails_as_read()


import time

while True:
    
    # check for text message response
    check_for_text_message_response()
    
    # Check for gamepad input for 0.1 seconds
    start_time = time.monotonic()
    while time.monotonic() - start_time < 0.1:
        # Read gamepad events if available
        try:
            event = gamepad.read_one()
        except BlockingIOError:
            event = None
        if event is not None:
            if event.type == ecodes.EV_KEY:
                data = categorize(event)
                # print(data)
                if data.keystate == 1:  # Button down
                    button = button_mappings.get(data.scancode)
                    print(f'Button {button} pressed')
                    if button == "1":
                        send_text_message(participants[0]) 
                    elif button == '2':
                        send_text_message(participants[1]) 
                    elif button == '3':
                        send_text_message(participants[2])
                    elif button == '4':
                        send_text_message(participants[3]) 
                    elif button == '5':
                        pass
                        # send_text_message(participants[4])
                    elif button == '6':
                        pass
                        # send_text_message(participants[5]) 
                    elif button == '7':
                        pass
                        # send_text_message(participants[6])
                    elif button == '8':
                        pass
                        # Try to close chrome
                        try:
                            os.system("killall -9 'chromedriver'")
                        except:
                            print("Can't close Chrome")


# continuously run program
# # while True:
    
# #     # check for text message response
# #     check_for_text_message_response()
# #     # print("im should be here a lot...")
# #     # Loop indefinitely and print button events
# #     for event in gamepad.read_loop():
# #         if event.type == ecodes.EV_KEY:
# #             data = categorize(event)
# #             # print(data)
# #             if data.keystate == 1:  # Button down
# #                 button = button_mappings.get(data.scancode)
# #                 print(f'Button {button} pressed')
# #                 if button == "1":
# #                     send_text_message(participants[0]) 
# #                 elif button == '2':
# #                     send_text_message(participants[1]) 
# #                 elif button == '3':
# #                     send_text_message(participants[2])
# #                 elif button == '4':
# #                     send_text_message(participants[3]) 
# #                 elif button == '5':
# #                     send_text_message(participants[4])
# #                 elif button == '6':
# #                     send_text_message(participants[5]) 
# #                 elif button == '7':
# #                     send_text_message(participants[6])
# #                 elif button == '8':
# #                     # close chrome
# #                     os.system("killall -9 'chromedriver'")
        
#     check_for_text_message_response()
#     print("I'm the end. Time to go again.")
