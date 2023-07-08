import argparse
import configparser

# Read the configuration file
config = configparser.ConfigParser()
config.read('config_global.ini')

# Using the global timeout and log_file before the overriding
timeout = config.get('Global', 'timeout')
log_file = config.get('Global', 'log_file')

# Use the configuration values in the application
print(timeout)
print(log_file)

# Create an ArgumentParser instance
parser = argparse.ArgumentParser()

# Define the command-line argument
parser.add_argument('--timeout', type=int, help='Specify the timeout value')

# Parse the command-line arguments
args = parser.parse_args()

# Access the specified timeout value
timeout = args.timeout

# Override the timeout value with the command-line argument, if provided
if timeout is not None:
    config.set('Global', 'timeout', str(timeout))

# Using the global timeout and log_file after the overriding
timeout = config.get('Global', 'timeout')
log_file = config.get('Global', 'log_file')

# Use the configuration values in the application
print(timeout)
print(log_file)
