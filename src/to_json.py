import json
from os import path



class JSONVault:
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, username, url, password,entropy):
        if not all([username, url, password]):
            raise ValueError("One or more fields are empty.")
        data = {"username": username, "url": url, "password": password, 'password_entropy': entropy}
        # Check if file exists
        if path.isfile(self.filename) is False:
            # Create a new JSON file with the data
            with open(self.filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
                print("JSON file created successfully.")
                json_file.close()

        else:
            # Load the existing JSON file
            with open(self.filename) as fp:
                existing_data = json.load(fp)
                fp.close()
            # iterate to see if duplicate url and if found update username and pw
            flag = False
            for item in existing_data:
                if item['url'] == data['url']:
                    item['password'] = data['password']
                    item['username'] = data['username']
                    item ['password_entropy'] = data['password_entropy']
                    with open(self.filename, 'w') as json_file:
                        json.dump(existing_data, json_file, indent=4)
                    print("JSON if")
                    json_file.close()
                    return

        # Else append the new data to the existing data
            existing_data.extend([data])
            # Write the updated data to the JSON file
            with open(self.filename, 'w') as json_file:
                json.dump(existing_data, json_file, indent=4)
                print("JSON else")
                json_file.close()
