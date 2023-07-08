import configparser

config = configparser.ConfigParser()
config.read('sample.INI')

# Handling missing or invalid configuration values from INI file
database_username = config.get('Database', 'username', fallback='adm')
database_password = config.get('Database', 'password', fallback='123456')
database_host = config.get('Database', 'host', fallback='localhost')
database_port = config.getint('Database', 'port', fallback=3306)

print(database_username)
print(database_password)
print(database_host)
print(database_port)