from selenium import webdriver
import geckodriver_autoinstaller
import time

geckodriver_autoinstaller.install() 

driver = webdriver.Firefox()
# test for registration
driver.get("http://localhost:4000/register")

driver.find_element_by_xpath('//*[@id="name"]').send_keys('SeleniumTest')
driver.find_element_by_xpath('//*[@id="designation"]').send_keys('Tester')
driver.find_element_by_xpath('//*[@id="department"]').send_keys('Test')
driver.find_element_by_xpath('//*[@id="username"]').send_keys('SeleniumTest')
driver.find_element_by_xpath('//*[@id="email"]').send_keys('seleniumtest@gmail.com')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('SeleniumTest')
driver.find_element_by_xpath('//*[@id="password2"]').send_keys('SeleniumTest')



driver.find_element_by_xpath('/html/body/div/div/div/form/button').submit()
time.sleep(10)

# Test for login
driver.get("http://localhost:4000/login")
driver.find_element_by_xpath('//*[@id="username"]').send_keys('SeleniumTest')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('SeleniumTest')
driver.find_element_by_xpath('/html/body/div/div/div/form/button').submit()


