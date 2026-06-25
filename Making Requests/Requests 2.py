import requests

# API endpoint for batch postcode lookup
POSTCODE_ENDPOINT = "https://api.postcodes.io/postcodes"

# Headers tell the API what format the request data is in
headers = {"Content-Type": "application/json"}

# Body contains the data we are sending (list of postcodes)
body = {
    "postcodes": ["PR3 0SG", "M45 6GN", "EX16 5BL"]
}

# Send POST request to the API
response = requests.post(
    POSTCODE_ENDPOINT,   # where we are sending the request
    headers=headers,     # metadata about the request (JSON format)
    json=body            # data automatically converted to JSON
)

# Convert API response (JSON string) into Python dictionary
data = response.json()

# Loop through each postcode result returned by the API
for item in data["result"]:

    # Check if postcode returned valid data
    if item["result"] is not None:

        # Print:
        # 1. original postcode sent
        # 2. eastings (grid X coordinate)
        # 3. northings (grid Y coordinate)
        print(
            item["query"],
            item["result"]["eastings"],
            item["result"]["northings"]
        )

    else:
        # If postcode is invalid or not found
        print(item["query"], "Invalid")
