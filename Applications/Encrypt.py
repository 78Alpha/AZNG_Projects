from Crypto import Random
from Crypto.Cipher import AES
import socket
import hashlib
import random

lib2 = [b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i', b'j', b'k', b'l', b'm', b'n', b'o', b'p', b'q',
        b'r', b's', b't', b'u', b'v', b'w', b'x', b'y', b'z', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8',
        b'9', b'0']


def key_gen_opt():
    random.seed(abs(sum(char_to_num_opt(hashlib.sha512("".join((str(socket.getfqdn()).split('.'))[1:]).encode('UTF-8')).hexdigest()))))  # Set seed to be a constant in the right facility, requires Amazon internal access
    random_key = b"".join([random.choice(lib2) for i in range(16)])
    return random_key


def num_check(item):
    if isinstance(item, int):
        return float(item)
    else:
        return ord(item.lower()) - 96


def char_to_num_opt(arg=None):
    new_list = [num_check(item) for item in arg]
    return new_list


def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


def encrypt(plaintext_data, key, key_size=256):
    data = pad(plaintext_data)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(data)


def encrypt_file(data, key):
    enc = encrypt(data, key)
    return enc


def decrypt(encrypted_data, key):
    iv = encrypted_data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext_data = cipher.decrypt(encrypted_data[AES.block_size:])
    return plaintext_data.rstrip(b"\0")


def decrypt_file(data, key):
    dec = decrypt(data, key)
    return dec


def get_link():
    key = key_gen_opt()
    enc_data = b'\xe1\xebs\x90\x0eo\xcdeQ\x1d\x08L<\x7f\x8e\xf2R\x17P\x04W\xf1lS\xb8.\x1d\xac\x92K\x01\x9c\xf4@\xa5E\xd7\x9e\xfaQ\xa9\xcc\xad\x7f\xfb\x8ct\x9b\x920"\x85\x13\x1e\xf4dQm\x8c\x9d\x81\x02)\x03'
    link = decrypt_file(enc_data, key).decode('UTF-8')
    return link
