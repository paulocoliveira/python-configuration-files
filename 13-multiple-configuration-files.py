import argparse
import configparser

# Create an ArgumentParser instance
parser = argparse.ArgumentParser()

# Define the command-line argument
parser.add_argument('--config', choices=['config_windows.ini', 'config_mac.ini', 'config_linux.ini'],
                    help='Specify the configuration file')

# Parse the command-line arguments
args = parser.parse_args()

# Access the specified configuration file
config_file = args.config

# Load the selected configuration file
config = configparser.ConfigParser()
config.read(config_file)

# Access the configuration values
driver_path = config.get('Browser', 'driver_path')
version = config.get('Browser', 'version')

# Utilize the configuration values in the test scenario
print(driver_path)
print(version)