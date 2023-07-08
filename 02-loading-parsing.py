import yaml

with open('sample.YAML', 'r') as file:
    config = yaml.safe_load(file)

# Accessing configuration values
username = config['DATABASE']['username']
password = config['DATABASE']['password']

print(username)
print(password)