from selenium import webdriver
import geckodriver_autoinstaller

geckodriver_autoinstaller.install() 

driver = webdriver.Firefox()
driver.get("https://www.onlinesbi.com/sbicollect/icollecthome.htm")
driver.find_element_by_xpath('//*[@id="proceedcheck_english"]').click()
driver.find_element_by_xpath('//*[@id="welcomecollect_english"]/div[2]/button').click()


driver.find_element_by_xpath('//*[@id="stateID"]/div/button').select('Kerala') #button
driver.find_element_by_xpath('//*[@id="instTypeID"]').select('Educational Institutions') #combobox
driver.find_element_by_xpath('//*[@id="go"]').click()
	
		#test to next stage
driver.get("https://www.onlinesbi.com/sbicollect/payment/listinstitution.htm")
driver.find_element_by_xpath('//*[@id="select-institute"]/div/button').select('COCHIN UNIVERSITY OF SCIENCE AND TECHNOLOGY (e-SBT)')  #button
driver.find_element_by_xpath('//*[@id="institutionform"]/div[2]/button[1]').click() #button
	
		#test to next stage
driver.get("https://www.onlinesbi.com/sbicollect/payment/listcategory.htm")
driver.find_element_by_xpath('//*[@id="frmFeeParams"]/div/div/div[2]/div/div[2]/div/button').select('Revaluation/Scrutiny/Condonation Fee Collection') #button

