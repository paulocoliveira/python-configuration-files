import json

with open('sample.json', 'r') as file:
    config = json.load(file)

# Accessing configuration values
username = config['Database']['username']
password = config['Database']['password']

print(username)
print(password)