import yaml

with open('sample.YAML', 'r') as file:
    config = yaml.safe_load(file)

# Handling missing or invalid configuration values from YAML file
database_username = config['DATABASE'].get('username', 'adm')
database_password = config['DATABASE'].get('password', '123456')
database_host = config['DATABASE'].get('host', 'localhost')
database_port = config['DATABASE'].get('port', 3306)

print(database_username)
print(database_password)
print(database_host)
print(database_port)