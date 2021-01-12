from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Define some stuff
browser  = webdriver.Chrome(ChromeDriverManager().install())
#platform = input("What platform do you want to use? Instagram or whatsapp. ")

# Start the browser and go to the site
browser.get('https://web.whatsapp.com')

# Check if the user is ready
while True:
    if input("If you want to go ahead and you have scanned the qr code type 'go ahead'. ") == "go ahead":
        break

# Define "send()"
def send(instagram):
    # Choose the person
    browser.find_element_by_css_selector("span[title='" + input("Enter the name or group to spam: ") + "']").click()

    # Enter the message
    inputString = input("Enter message to send: ")
    print("Started spamming! If you want to stop it press Ctrl+C.")

    # Send the messages
    try:
        while True:
            browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
            browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()

    except KeyboardInterrupt:
        print("Stopped spamming...")
        pass

# Send the messages
while True:
    send("instagram")
