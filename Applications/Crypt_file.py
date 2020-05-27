from Crypto.Cipher import AES
import codecs
import socket
import secrets
import math
import random
import hashlib
import codecs
import webbrowser
import base64
import json

_HOST_NAME_ = str(socket.getfqdn())

_Master_Hash_ = "79d4871b65ae571ce1917646a2eb8e9889b2be51d60406278e14e14dab90aedb0c231aa38788d512e35b4197033fbabecd7c3d24016e6baeca9ea3d164df11e1"


def char_to_num(arg=None):
    new_list = []
    for item in arg:
        try:
            valueless = item / 1.0
            new_list.append(float(item))
        except:
            new_list.append((ord(item.lower()) - 96))
    return new_list


def hashing(arg=None):
    step1 = hashlib.sha512(arg.encode('UTF-8'))
    # step2 = step1.update()
    step2 = step1.hexdigest()
    return step2


def extension(hash=None):
    master = 1.0
    count = 0
    back_variable = 0.0
    if (len(hash) % 2) == 0:
        for item in hash:
            master *= item
    else:
        return "ERR"
    return master


def seed_maker():
    random.seed(extension(char_to_num(hashing(_HOST_NAME_))))

    rand_check_value = random.randint(2 ** 32, 2 ** 64)

    if hashing(str(rand_check_value)) == _Master_Hash_:
        return rand_check_value

key = seed_maker()


def cipher_module_encrypt(key=None, data=None):

    encryption_mode = AES.new(key, AES.MODE_EAX)

    nonce = encryption_mode.nonce

    crypt_bytes, tag = encryption_mode.encrypt_and_digest(bytes(data.encode('UTF-8')))

    with open("Crypted_Info.file", 'w+') as crypt_put:
        temp_keys = {"TAG" : base64.encodebytes(tag).decode('ascii'), "NONCE" : base64.encodebytes(nonce).decode('ascii')}
        json.dump(temp_keys, crypt_put)

    with open("sha512.file", 'wb+') as sha_out:
        sha_out.write(crypt_bytes)

    return crypt_bytes, tag, nonce


def cipher_module_decrypt(crypted_data=None, nonce=None, key=None, tag=None):
    with open("sha512.file", 'rb') as info:
        data = info.read()
        info.close()
    with open("Crypted_Info.file", 'r') as crypt_info:
        crypt_lines = json.load(crypt_info)
        crypt_info.close()
    tag = bytes(base64.decodebytes(crypt_lines["TAG"].encode('ascii')))
    nonce = bytes(base64.decodebytes(crypt_lines["NONCE"].encode('ascii')))
    enc_method = AES.new(key, AES.MODE_EAX, nonce=nonce)
    link = enc_method.decrypt(crypted_data)
    try:
        enc_method.verify(tag)
        return link.decode('UTF-8')
    except ValueError:
        return "INVALID"


data = open("LICENSE", 'r').read()

crypted, tag, nonce = cipher_module_encrypt(key=bytes(str(key)[3:].encode('UTF-8')), data=data)
return_data = cipher_module_decrypt(crypted_data=crypted, key=bytes(str(key)[3:].encode('UTF-8')))

print(len(return_data) > 0)
