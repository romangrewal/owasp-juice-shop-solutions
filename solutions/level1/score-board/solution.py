from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import jsbeautifier
import os

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
  search_string = input("Enter search route: ")
  #Fetch HTML content (user opens browser)
  url = f"http://'{IP_ADDRESS}':'{PORT}'"
  response = requests.get(url)
  html_content = response.text

  driver = webdriver.Chrome()
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
      driver.get(f"http://'{IP_ADDRESS}':'{PORT}'/#/" + search_string)

finally:
  driver.quit()
