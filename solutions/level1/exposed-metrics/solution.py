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

	#User visits OWASP Juice Shop
	driver.get(f"http://{IP_ADDRESS}:{PORT}")

	#User navigates to exposed metrics page
	driver.get(f"http://{IP_ADDRESS}:{PORT}/metrics")
	
finally:
  driver.quit()
