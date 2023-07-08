import configparser

# Load the global configuration file
config = configparser.ConfigParser()
config.read('config_global.ini')

# Using the global timeout and log_file
timeout = config.get('Global', 'timeout')
log_file = config.get('Global', 'log_file')

print(timeout)
print(log_file)

# Override specific configuration values for a test
config.set('Test', 'timeout', '90')
config.set('Test', 'log_file ', 'new_test_logs.txt')

# Access configuration values with the overridden value
timeout = config.get('Test', 'timeout')
log_file = config.get('Test', 'log_file')

print(timeout)
print(log_file)