import yaml

with open('config.YAML', 'r') as file:
    config = yaml.safe_load(file)

# Access the configuration values
api_endpoint = config['API']['endpoint']
timeout = config['API']['timeout']

# Validate the timeout value
if isinstance(timeout, int) and timeout > 0:
    print(f"Timeout value is valid: {timeout} seconds")
else:
    print("Invalid timeout value. Please provide a positive integer.")