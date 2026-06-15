import requests
def check_if_pwned(email):
    import hashlib
    sha1_hash = hashlib.sha1(email.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    if response.status_code != 200:
        raise Exception("Error fetching data from Have I Been Pwned API.")
    
    hashes = response.text.splitlines()
    for line in hashes:
        h, count = line.split(':')
        if h == sha1_hash[5:]:
            return True, count  
    return False, 0  

email = input("Enter your email: ")
pwned, count = check_if_pwned(email)
if pwned:
    print(f"Your email has been pwned {count} times.")
else:
    print("Your email has not been pwned.")