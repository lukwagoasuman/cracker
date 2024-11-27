import hashlib

def crack_sha1_hash(hash_to_crack, use_salts=False):
    # Paths to the files
    passwords_file = 'top-10000-passwords.txt'
    salts_file = 'known-salts.txt'

    # Read passwords from file
    with open(passwords_file, 'r') as file:
        passwords = [line.strip() for line in file]

    # If salts are to be used, read them from the file
    salts = []
    if use_salts:
        with open(salts_file, 'r') as file:
            salts = [line.strip() for line in file]

    # Hash each password and check against the given hash
    for password in passwords:
        # Simple hash check without salts
        if hashlib.sha1(password.encode()).hexdigest() == hash_to_crack:
            return password

        # If salts are used, hash with each salt (both prepend and append)
        if use_salts:
            for salt in salts:
                # Prepend salt
                if hashlib.sha1((salt + password).encode()).hexdigest() == hash_to_crack:
                    return password
                # Append salt
                if hashlib.sha1((password + salt).encode()).hexdigest() == hash_to_crack:
                    return password

    return "PASSWORD NOT IN DATABASE"
