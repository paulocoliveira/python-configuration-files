import json

with open('sample.json', 'r') as file:
    config = json.load(file)

# Handling missing or invalid configuration values from JSON file
database_username = config['Database'].get('username', 'adm')
database_password = config['Database'].get('password', '123456')
database_host = config['Database'].get('host', 'localhost')
database_port = config['Database'].get('port', 3306)

print(database_username)
print(database_password)
print(database_host)
print(database_port)