from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

try:
	driver = webdriver.Chrome()

	#User visits OWASP Juice Shop
	driver.get("http://192.168.0.217:3000")

	#User navigates to exposed metrics page
	driver.get("http://192.168.0.217:3000/metrics")
	
finally:
  driver.quit()
