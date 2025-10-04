from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

try:
	driver = webdriver.Chrome()
	driver.get("http://192.168.0.217:3000")

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

	#User navigates to Privacy Policy
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Account')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Privacy & Security')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Privacy Policy')]"))).click()
	
finally:
  driver.quit()
