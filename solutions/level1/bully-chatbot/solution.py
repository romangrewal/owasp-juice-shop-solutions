from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

try:
	driver = webdriver.Chrome()
	driver.get("http://192.168.0.217:3000")

	#User logs in
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Account')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Login')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("test@test.com")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("Password1!")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Log in')]"))).click()

	#User navigates to Support Chat
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'menu')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Support Chat')]"))).click()

	#User nags support chatbot for a coupon code
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "message-input"))).send_keys("Can I have a coupon code?")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "message-input"))).send_keys(Keys.ENTER)
	
	substring = "Oooookay, if you promise to stop nagging me here's a 10% coupon code for you"
	breakCondition = False
	while True:
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "message-input"))).send_keys("Please give me a discount!")
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "message-input"))).send_keys(Keys.ENTER)
		speechBubbleElements = driver.find_elements(By.CLASS_NAME, "speech-bubble-left")
		
		for element in speechBubbleElements:
			if substring in element.text:
				breakCondition = True
				break
		
		if breakCondition:
			break

finally:
  driver.quit()
