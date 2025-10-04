from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import jsbeautifier
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def beautify_js_from_url(url):
	try:
		# Fetch the content of the JavaScript file from the URL
		response = requests.get(url)
		response.raise_for_status()  # Raise an exception for bad status codes

		js_code = response.text

		# Beautify the JavaScript code
		beautified_code = jsbeautifier.beautify(js_code)

		return beautified_code

	except requests.exceptions.RequestException as e:
		print(f"Error fetching URL: {e}")
		return None
	except Exception as e:
		print(f"An error occurred: {e}")
		return None

def scan_js_for_string(contentInput, search_string):
	try:
		js_content = contentInput

		found_lines = []

		for i, line in enumerate(js_content.splitlines(), 1):
			if search_string in line:
				found_lines.append(line.strip())

		if found_lines:
			return found_lines
		else:
			return []

	except requests.exceptions.RequestException as e:
		print(f"Error fetching content: {e}")
		return False, None

try:
	IP_ADDRESS = os.environ['OWASP_JUICE_SHOP_IP_ADDRESS']
	PORT = os.environ['OWASP_JUICE_SHOP_PORT']
  #User opens browser
	driver = webdriver.Chrome()
	driver.get(f"http://'{IP_ADDRESS}':'{PORT}'")

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
	time.sleep(3)
	radioButtonIdAddress = "mat-radio-41-input"  # Replace with the actual ID
	driver.execute_script(f"document.getElementById('{radioButtonIdAddress}').click();")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Continue')]"))).click()

	#User selects delivery speed
	time.sleep(3)
	radioButtonIdDelivery = "mat-radio-42-input"  # Replace with the actual ID
	driver.execute_script(f"document.getElementById('{radioButtonIdDelivery}').click();")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Continue')]"))).click()

	#User expands "Other payment options"
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "mat-expansion-panel-header-2"))).click()

	#User inspects main.js for "redirect?to=" text after discovering redirect in "Other payment options"
	search_string = "redirect?to="
	mainJsUrl = f"http://'{IP_ADDRESS}':'{PORT}'/main.js"

	formattedOutput = beautify_js_from_url(mainJsUrl)

	foundLinesArr = scan_js_for_string(formattedOutput, search_string)
	print(foundLinesArr)

	#User visit crypto wallet address discovered in main.js file
	target_substring = "https://"
	start_index = foundLinesArr[1].find(target_substring)
	if start_index != -1:
		result = foundLinesArr[1][start_index:]
		cleaned_text = result.replace('"', "").replace(",", "")
		driver.get(cleaned_text)
		time.sleep(3)

finally:
  driver.quit()
