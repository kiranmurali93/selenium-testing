# Chat bot testing
import time
from selenium import webdriver
import geckodriver_autoinstaller

geckodriver_autoinstaller.install() 

driver = webdriver.Firefox()
driver.get("https://node-red-qoajg-2020-10-28.eu-gb.mybluemix.net/ui/#!/0?socketid=BDCALMAVAR_bBLOSAAAc")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="WACLauncher__Button"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="downshift-0-toggle-button"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="downshift-0-item-1"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="downshift-6-toggle-button"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="downshift-6-item-3"]/div').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="WAC__message-5"]/div/div/div[3]/div[2]/ul/li[1]/button').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="WAC__message-7"]/div/div/div[3]/div[2]/ul/li[2]/button').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="WAC__message-10"]/div/div/div[2]/div[2]/ul/li[1]/button').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="WAC__message-13"]/div/div/div[2]/div[2]/ul/li[2]/button').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="WAC__message-16"]/div/div/div[2]/div[2]/ul/li[3]/button').click()
