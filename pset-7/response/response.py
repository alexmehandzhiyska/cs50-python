import validator_collection

email = input('Email: ')

is_valid = 'Valid' if validator_collection.is_email(email) else 'Invalid'
print(is_valid)