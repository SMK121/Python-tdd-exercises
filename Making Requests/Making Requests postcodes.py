

import requests

# Base URL for the Postcodes.io API
POSTCODE_ENDPOINT = "https://api.postcodes.io/postcodes/"

# Make a GET request to the API with a specific postcode
response = requests.get(POSTCODE_ENDPOINT + "EC2Y5AS")

# Print the raw HTTP response object (e.g. <Response [200]> means success)
print(response)

# Only continue if the request was successful (200 = OK)
if response.status_code == 200:

    # Convert the JSON response into a Python dictionary
    response_json = response.json()

    # Print the top-level keys in the dictionary (e.g. 'status', 'result')
    print(response_json.keys())

    # Extract the actual postcode data (this is where all useful info is stored)
    result = response_json["result"]

    # Print the full result dictionary (all postcode information)
    print(result)

