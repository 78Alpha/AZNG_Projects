import hashlib


def hash_password(password):
    pass_hash = hashlib.sha256(password.encode()).hexdigest()
    return pass_hash

def compare_password(password):
    # print(password)
    expected_hash = "18c4afb5bb674df5f22a1ad2818eae52a7e2af5cd9dc6143e09284f18f03e07f"
    pass_hash = hash_password(password)
    # print(password, pass_hash, expected_hash, pass_hash == expected_hash)
    return pass_hash == expected_hash
