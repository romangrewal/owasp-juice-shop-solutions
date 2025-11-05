from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

try:
	IP_ADDRESS = os.environ['OWASP_JUICE_SHOP_IP_ADDRESS']
	PORT = os.environ['OWASP_JUICE_SHOP_PORT']
	#Disable the password manager's leak detection
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_experimental_option("prefs", {
		"profile.password_manager_leak_detection": False,
		"credentials_enable_service": False,  # Disables the "save password" prompt
		"profile.password_manager_enabled": False # Disables the password manager entirely
	})

  #User opens browser
	driver = webdriver.Chrome(options=chrome_options)
	driver.get(f"http://{IP_ADDRESS}:{PORT}")

	#User logs in
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Account')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Login')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("mc.safesearch@juice-sh.op")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("Mr. N00dles")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Log in')]"))).click()

	input("Press Enter...")

finally:
  driver.quit()
