import json
from os import path

username = "Cow"
url = "https://github.com/vibqetowi/team-placeholder-conuhacksVII"
password = "9888"

if not all([username, url, password]):
    raise ValueError("One or more fields are empty.")

data = [{"username": username, "url": url, "password": password}]
filename = './vault.json'

# Check if file exists
if path.isfile(filename) is False:
    # Create a new JSON file with the data
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        print("JSON file created successfully.")
else:
    # Load the existing JSON file
    with open(filename) as fp:
        existing_data = json.load(fp)
    # Append the new data to the existing data
    existing_data.extend(data)
    # Write the updated data to the JSON file
    with open(filename, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)
        print("Data successfully appended to the JSON file.")
