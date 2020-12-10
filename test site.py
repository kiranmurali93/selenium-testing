from selenium import webdriver
import geckodriver_autoinstaller
import time
geckodriver_autoinstaller.install()
driver = webdriver.Firefox()

#//*[@id="user_title"]/option[1]
#//*[@id="user_title"]

#test for registration
driver.get("http://demo.guru99.com/insurance/v1/register.php")

driver.find_element_by_xpath('//*[@id="user_title"]/option[1]').click()

driver.find_element_by_xpath('//*[@id="user_firstname"]').send_keys('Selenium')

driver.find_element_by_xpath('//*[@id="user_surname"]').send_keys('Test')

driver.find_element_by_xpath('//*[@id="user_phone"]').send_keys('5566778899')

driver.find_element_by_xpath('//*[@id="user_dateofbirth_1i"]/option[61]').click()

driver.find_element_by_xpath('//*[@id="user_dateofbirth_2i"]/option[7]').click()

driver.find_element_by_xpath('//*[@id="user_dateofbirth_3i"]/option[21]').click()

driver.find_element_by_xpath('//*[@id="licencetype_t"]').click()

driver.find_element_by_xpath('//*[@id="user_licenceperiod"]/option[4]').click()

driver.find_element_by_xpath('//*[@id="user_occupation_id"]/option[1]').click()

driver.find_element_by_xpath('//*[@id="user_address_attributes_street"]').send_keys('XYZ street')

driver.find_element_by_xpath('//*[@id="user_address_attributes_city"]').send_keys('delhi')

driver.find_element_by_xpath('//*[@id="user_address_attributes_county"]').send_keys('india')

driver.find_element_by_xpath('//*[@id="user_address_attributes_postcode"]').send_keys('123456') 

driver.find_element_by_xpath('//*[@id="user_user_detail_attributes_email"]').send_keys('xyz@gmail.com')

driver.find_element_by_xpath('//*[@id="user_user_detail_attributes_password"]').send_keys('xyz')

driver.find_element_by_xpath('//*[@id="user_user_detail_attributes_password_confirmation"]').send_keys('xyz')

driver.find_element_by_xpath('//*[@id="new_user"]/div[5]/input[2]').click()

time.sleep(15)

#test for login

driver.get("http://demo.guru99.com/insurance/v1/index.php")

driver.find_element_by_xpath('//*[@id="email"]').send_keys('xyz@gmail.com')

driver.find_element_by_xpath('//*[@id="password"]').send_keys('xyz')

driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()
time.sleep(15)

#test for logout

driver.get("http://demo.guru99.com/insurance/v1/header.php")

driver.find_element_by_xpath('/html/body/div[3]/form/input').click()
