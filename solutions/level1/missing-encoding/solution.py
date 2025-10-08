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
	driver.get(f"http://{IP_ADDRESS}:{PORT}")

	#User navigates to Photo Wall
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'menu')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Photo Wall')]"))).click()

	#User inspects src to find broken image url
	alt_text = "😼 #zatschi #whoneedsfourlegs"
	broken_image_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//img[@alt='{alt_text}']")))
	broken_src = broken_image_element.get_attribute("src")

	#User visits absolute url with copy-pasted image url
	base_domain = f"http://{IP_ADDRESS}:{PORT}/"
	broken_full_url = base_domain + broken_src
	driver.get(broken_full_url)

	#User fixes encoding to reveal image
	corrected_relative_path = broken_src.replace("#", "%23")
	corrected_full_url = base_domain + corrected_relative_path
	driver.get(corrected_full_url)	

finally:
  driver.quit()
