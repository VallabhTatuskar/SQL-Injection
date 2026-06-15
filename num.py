import hashlib

# Predefined mock response with hash suffixes for known pwned numbers
mock_response = {
    'A0A1B2C3': 5,  # Replace with actual hash suffix for a known pwned number
    'DDE12': 3,     # Example suffix, replace with calculated suffix
    'F1234ABCD': 4  # Another example, replace with actual suffix
}

def check_if_number_pwned(phone_number):
    # Get the SHA-1 hash of the phone number
    sha1_hash = hashlib.sha1(phone_number.encode('utf-8')).hexdigest().upper()
    hash_suffix = sha1_hash[5:]

    # Check if the hash suffix is in the predefined mock response
    if hash_suffix in mock_response:
        return True, mock_response[hash_suffix]  # Phone number is pwned, return the count
    
    return False, 0  # Phone number is not pwned

# Example usage
phone_number = input("Enter your phone number: ")
pwned, count = check_if_number_pwned(phone_number)
if pwned:
    print(f"Your phone number has been pwned {count} times.")
else:
    print("Your phone number has not been pwned.")
