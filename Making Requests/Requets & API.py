import requests

POSTCODE_ENDPOINT = "https://api.postcodes.io/postcodes"

# Makeup of a request #Headers #Body

# Headers tell the API what format the data is in
headers = {"Content-Type": "application/json"}

# Body contains the data we are sending (list of postcodes to look up)
body = {
    "postcodes": ["PR3 0SG", "M45 6GN", "EX16 5BL"]
}

# Send a POST request to the postcode API
response = requests.post(
    url=POSTCODE_ENDPOINT,   # API endpoint we are sending data to
    headers=headers,         # request metadata (format info)
    json=body                # data being sent (auto-converted to JSON)
)




# Print the full response object
print(response)

# Print status code + raw response content
print(response.status_code, response.content)