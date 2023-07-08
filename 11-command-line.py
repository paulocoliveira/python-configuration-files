import argparse
import configparser

# Read the configuration file
config = configparser.ConfigParser()
config.read('config_envs.ini')

# Create an ArgumentParser instance
parser = argparse.ArgumentParser()

# Define the command-line argument
parser.add_argument('--environment', choices=['Development', 'Staging', 'Production'], default='development',
                    help='Specify the test environment')

# Parse the command-line arguments
args = parser.parse_args()

# Access the specified environment
environment = args.environment

# Use the test configuration based on the specified environment
database_url = config.get(environment, 'database_url')
api_key = config.get(environment, 'api_key')

# Use the configuration values in the application
print(database_url)
print(api_key)
