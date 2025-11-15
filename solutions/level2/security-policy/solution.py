from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

try:
	IP_ADDRESS = os.environ['OWASP_JUICE_SHOP_IP_ADDRESS']
	PORT = os.environ['OWASP_JUICE_SHOP_PORT']

  #User opens browser to security disclosure page
	driver = webdriver.Chrome(options=chrome_options)
	driver.get(f"http://{IP_ADDRESS}:{PORT}/.well-known/security.txt")

	input("Press Enter...")

	driver.get(f"http://{IP_ADDRESS}:{PORT}")

	input("Press Enter...")

finally:
  driver.quit()
