from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Define some stuff
browser  = webdriver.Chrome(ChromeDriverManager().install())
ready_message = "go ahead"

# Start the browser and go to the site
browser.get('https://web.whatsapp.com')

# Check if the user is ready
ready = input("If you want to go ahead and you have scanned the qr code type 'go ahead'")

while True:
    if ready == ready_message:
        break

# Print if it is working
print("logged in")

# Choose the person
browser.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()

# Enter the message
inputString = input("Enter message to send: ")

# Send the messages
while True:
    browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
