import configparser

config = configparser.ConfigParser()
config.read('sample.INI')

# Accessing configuration values
url = config.get('General', 'url')
selenium_version = config.get('General', 'selenium_version')
timeout = config.get('General', 'timeout')

print(url)
print(selenium_version)
print(timeout)