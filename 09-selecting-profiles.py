import configparser

# Read the configuration file
config = configparser.ConfigParser()
config.read('config_envs.ini')

# Get the environment from an environment-specific variable
environment = 'Staging'

# Access the configuration values for the selected environment
database_url = config.get(environment, 'database_url')
api_key = config.get(environment, 'api_key')

# Use the configuration values in the application
print(database_url)
print(api_key)