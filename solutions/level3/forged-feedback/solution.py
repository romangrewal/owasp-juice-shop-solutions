import requests

# Define the API endpoint URL
url = "http://192.168.0.118:3000/api/Feedbacks/" # Example public API

# Prepare the JSON payload for the request body
payload = {"UserId":1,"captchaId":1,"captcha":"5","comment":"asg (***t@test.com)","rating":2}

# Send the POST request with the JSON payload
response = requests.post(url, json=payload)

# Print the response status code and JSON content
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.json()}")
