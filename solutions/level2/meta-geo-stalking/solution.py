from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import subprocess
import os
import geopy
from geopy.geocoders import GoogleV3

def extract_coordinates(image_path):
	command = ['exiftool', '-gpslatitude', '-gpslongitude', '-n', '-s3', image_path]
	try:
		process = subprocess.run(command, capture_output=True, text=True, check=True)
		output_lines = process.stdout.strip().split('\n')
        
		if len(output_lines) != 2:
			raise ValueError("ExifTool did not return two coordinate values.")

		latitude = float(output_lines[0])
		longitude = float(output_lines[1])
		return latitude, longitude
    
	except Exception as e:
		print(f"❌ Error extracting coordinates: {e}")
		return None

def get_forest_name_google(latitude, longitude, api_key):
	try:
		geolocator = GoogleV3(api_key=api_key, user_agent="google-forest-locator")

		location = geolocator.reverse((latitude, longitude), exactly_one=False, language='en')

		if not location:
			return "No location results found near those coordinates."

		for result in location:
			for component in result.raw.get('address_components', []):
				component_name = component.get('long_name', '')

				if any(word in component_name.lower() for word in ['forest', 'park', 'reserve']):
					types = result.raw.get('types', [])
					if 'natural_feature' in types or 'park' in types or 'establishment' in types:
						return f"🌳 Found Forest/Park Name: {component_name}"

		return f"Nearest Address: {location[0].address} (Forest name not explicitly listed in API result types.)"

	except Exception as e:
		return f"Google Maps Geocoding failed: {e}"

try:
	IP_ADDRESS = os.environ['OWASP_JUICE_SHOP_IP_ADDRESS']
	PORT = os.environ['OWASP_JUICE_SHOP_PORT']
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_experimental_option("prefs", {
		"profile.password_manager_leak_detection": False,
		"credentials_enable_service": False,
		"profile.password_manager_enabled": False
	})
	driver = webdriver.Chrome(options=chrome_options)
	driver.get(f"http://{IP_ADDRESS}:{PORT}")
	
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Dismiss')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'menu')]"))).click()
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Photo Wall')]"))).click()

	image_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='I love going hiking here... (© j0hNny)']")))
	image_url = image_element.get_attribute("src")
	urllib.request.urlretrieve(image_url, "downloaded_image.png")

	image_file_path = os.getcwd() + '/downloaded_image.png' # Replace with your image file path
	print(image_file_path)

	coords = extract_coordinates(image_file_path)

	if coords:
		lat, lon = coords
		GOOGLE_API_KEY = os.environ['GOOGLE_MAPS_API']

		print("Attempting reverse geocoding using Google Maps API...")
		forest_result = get_forest_name_google(lat, lon, GOOGLE_API_KEY)

		print("\n-------------------------------------------------")
		print(f"🌲 **Location Name Result:**")
		print(forest_result)

finally:
  driver.quit()
