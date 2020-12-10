#python program to get number of subscribers in my channel using selenium
#works with firefox
from selenium import webdriver
import geckodriver_autoinstaller

geckodriver_autoinstaller.install() 

driver = webdriver.Firefox()
driver.get("https://www.youtube.com/channel/UC5rb-lnd-4rtJqRIAWurURA")

subscriber_Count = driver.execute_script('return document.querySelector("#subscriber-count")')
print(subscriber_Count.get_attribute('innerHTML'))
