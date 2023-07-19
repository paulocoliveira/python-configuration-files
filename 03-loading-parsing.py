import json

with open('sample.json', 'r') as file:
    config = json.load(file)

# Accessing configuration values
url = config['General']['url']
selenium_version = config['General']['selenium_version']
timeout = config['General']['timeout']

print(url)
print(selenium_version)
print(timeout)