import smtplib
import imaplib
import email
# import webbrowser
import keyboard
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
import time

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

# function to send text message
def send_text_message():
    # get user input for phone number, carrier, and message
    # phone_number = input('Enter phone number: ')
    # carrier = input('Enter carrier (verizon, att, sprint, tmobile): ')
    # message = input('Enter message: ')

    phone_number='3852410787'
    carrier='verizon'
    message='Ladd and Selassie want to Facetime! Reply to this message with a Facetime link.'

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

    options = webdriver.ChromeOptions()
    options.add_argument(r'--use-fake-ui-for-media-stream') #e.g. Profile 3

    # set up the webdriver
    browser = webdriver.Chrome(chrome_options=options)

    browser.get(message_url) # replace with the URL of the webpage you want to automate
    time.sleep(10)
    # find the input field by its ID and enter "Ladd and Selassie"
    input_field = browser.find_element_by_id("name-entry")
    input_field.clear()
    input_field.send_keys("Ladd and Selassie")

    # click the "Continue" button
    continue_button = browser.find_element_by_xpath("//ui-button[@aria-label='Continue']")
    continue_button.click()

    # wait for the page to load
    time.sleep(5)

    try:
        # allow access to microphone and camera
        microphone = browser.find_element_by_xpath('//div[@class="permission-checkbox mic"]')
        microphone.click()
        camera = browser.find_element_by_xpath('//div[@class="permission-checkbox cam"]')
        camera.click()
    except:
        print("not there")


    # click the "Join" button by its ID
    join_button = browser.find_element_by_id("callcontrols-join-button-session-banner")
    join_button.click()

    # wait for the page to load
    time.sleep(2)

    # click the SVG button
    # svg_button = browser.querySelector('#callcontrols-video-button');
    # svg_button.click()
    # time.sleep(2)

    # click the fullscreen button
    fullscreen_button = browser.find_element_by_css_selector('#callcontrols-fullscreen-button')
    fullscreen_button.click()

    # wait for the page to load
    time.sleep(100)

    # # parse the HTML using BeautifulSoup and do something with it
    # soup = BeautifulSoup(browser.page_source, "html.parser")
    # # do something with the parsed HTML

    # close the browser window
    browser.close()


def check_for_text_message_response():
    # login to IMAP server
    mail = imaplib.IMAP4_SSL(imap_server, imap_port)
    mail.login(email_address, email_password)
    mail.select("inbox")

    # search for messages
    result, data = mail.search(None, "ALL")
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

        # delete message from mailbox
        mail.store(num, '+FLAGS', '\\Deleted')

    # expunge deleted messages from mailbox
    mail.expunge()
    mail.close()
    mail.logout()



# # continuously run program
while True:
    # check for text message response
    check_for_text_message_response()

    # check for user input to send message
    if keyboard.is_pressed(' '): 
        print('message')
        send_text_message() 

    # pause program for 5 seconds before checking again
    # time.sleep(5)


# check_for_text_message_response()