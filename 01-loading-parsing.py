import configparser

config = configparser.ConfigParser()
config.read('sample.INI')

# Accessing configuration values
username = config.get('Database', 'username')
password = config.get('Database', 'password')

print(username)
print(password)