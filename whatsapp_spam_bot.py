from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Define some stuff
browser  = webdriver.Chrome(ChromeDriverManager().install())
ready_message = "go ahead"
ready_to_send_message = "send"

# Start the browser and go to the site
browser.get('https://web.whatsapp.com')

# Check if the user is ready
ready = input("If you want to go ahead and you have scanned the qr code type '" + ready_message + "' ")

while True:
    if ready == ready_message:
        break

# Define "send()"
def send():
    # Choose the person
    browser.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()

    # Enter the message
    inputString = input("Enter message to send: ")

    # Send the messages
    try:
        while True:
            browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
            browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()

    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate while statement")
        pass


# Choose what to do
#what_do_you_want_to_do = input("What do you want to do? ")

# Spam
while True:
    if input("What do you want to do? ") == "send":
        send()
