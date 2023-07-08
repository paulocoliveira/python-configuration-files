import configparser
import os

# Load the global configuration file
config = configparser.ConfigParser()
config.read('config_global.ini')

# Using the global timeout and log_file
timeout = config.get('Global', 'timeout')
log_file = config.get('Global', 'log_file')

print(timeout)
print(log_file)

# Retrieve the database connection string from the environment variable
env_timeout = os.getenv('GLOBAL_TIMEOUT')

# Override specific configuration values for a test
config.set('Global', 'timeout', env_timeout)

# Access configuration values with the overridden value
timeout = config.get('Global', 'timeout')
log_file = config.get('Global', 'log_file')

print(timeout)
print(log_file)