import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read('config_complex.ini')

# Retrieve the user's location from a user profile or request context
user_location = 'UK'

# Apply conditional configurations based on the user's location
if user_location == 'US':
    currency = config.get('US', 'currency')
    shipping_option = config.get('US', 'shipping_option')
elif user_location == 'UK':
    currency = config.get('UK', 'currency')
    shipping_option = config.get('UK', 'shipping_option')
else:
    currency = config.get('default', 'currency')
    shipping_option = config.get('default', 'shipping_option')

# Utilize the selected configuration values in your test execution
print("User Location: " + user_location)
print("Currency: " + currency)
print("Shipping Option: " + shipping_option)
