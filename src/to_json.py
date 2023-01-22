import json
from os import path

class JSONVault:
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, username, url, password):
        if not all([username, url, password]):
            raise ValueError("One or more fields are empty.")
        data = [{"username": username, "url": url, "password": password}]
        # Check if file exists
        if path.isfile(self.filename) is False:
            # Create a new JSON file with the data
            with open(self.filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
                print("JSON file created successfully.")
        else:
            # Load the existing JSON file
            with open(self.filename) as fp:
                existing_data = json.load(fp)
            # Append the new data to the existing data
            existing_data.extend(data)
            # Write the updated data to the JSON file
            with open(self.filename, 'w') as json_file:
                json.dump(existing_data, json_file, indent=4)
                print("Data successfully appended to the JSON file.")

vault = JSONVault('./vault.json')
vault.write_data("Cow", "https://github.com/vibqetowi/team-placeholder-conuhacksVII", "9888")

