from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os

try:
	IP_ADDRESS = os.environ['OWASP_JUICE_SHOP_IP_ADDRESS']
	PORT = os.environ['OWASP_JUICE_SHOP_PORT']
	driver = webdriver.Chrome()
	driver.get(f"http://'{IP_ADDRESS}':'{PORT}'")

	#User navigates to About Us Page
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'menu')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'About Us')]"))).click()

	#User clicks on "Check out our boring terms of use if you are interested in such lame stuff" link
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'About Us')]"))).click()

	#User attempts to browse directory by changing the url to http://<ip>:<port>/ftp
	driver.get("http://192.168.0.217:3000/ftp")

	#User accesses confidential document
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'acquisitions.md')]"))).click()

finally:
  driver.quit()
