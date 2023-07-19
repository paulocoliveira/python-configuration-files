import yaml

with open('sample.YAML', 'r') as file:
    config = yaml.safe_load(file)

# Accessing configuration values
url = config['GENERAL']['url']
selenium_version = config['GENERAL']['selenium_version']
timeout = config['GENERAL']['timeout']

print(url)
print(selenium_version)
print(timeout)