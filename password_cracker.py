import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # Load top-10000-passwords.txt
    with open('top-10000-passwords.txt', 'r') as password_file:
        passwords = [line.strip() for line in password_file]
    
    # Load known-salts.txt if use_salts is True
    salts = []
    if use_salts:
        with open('known-salts.txt', 'r') as salts_file:
            salts = [line.strip() for line in salts_file]

    # Compare each password (with and without salts) against the hash
    for password in passwords:
        # Hash the password without salt
        if hashlib.sha1(password.encode()).hexdigest() == hash:
            return password
        
        # If use_salts is enabled, hash the password with salts
        if use_salts:
            for salt in salts:
                # Append salt
                salted_password = password + salt
                if hashlib.sha1(salted_password.encode()).hexdigest() == hash:
                    return password

                # Prepend salt
                salted_password = salt + password
                if hashlib.sha1(salted_password.encode()).hexdigest() == hash:
                    return password

    # If no match is found, return string
    return "PASSWORD NOT IN DATABASE"
