import configparser
import platform

# Get the OS version
os_version = platform.system()

# Determine the corresponding configuration file based on the OS version
if os_version == 'Windows':
    config_file = 'config_windows.ini'
elif os_version == 'Darwin':
    config_file = 'config_mac.ini'
elif os_version == 'Linux':
    config_file = 'config_linux.ini'
else:
    config_file = 'config.ini'  # Default configuration file

# Load the configuration file
config = configparser.ConfigParser()
config.read(config_file)

# Access the configuration values
driver_path = config.get('Browser', 'driver_path')
version = config.get('Browser', 'version')

# Utilize the configuration values in the test scenario
print(driver_path)
print(version)