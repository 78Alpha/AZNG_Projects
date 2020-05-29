import PySimpleGUI as gui
import os
import pyautogui
import time
import sys
import webbrowser
import socket
import hashlib
import random
import pathlib
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Cipher import AES


"""
    Function: key_gen() | Uses the net_interface to generate a unique key and hash it fo later use, is not functional on its own
"""


def key_gen():
    """
    :var host_list: Get the host name from current network, expects ASIN282 access
    :var _HOST_NAME_: Join host parts without front face unique tag, this allows use of all internal computers
    :var _Hash_Master_: Hashes the host name into a unique key using modern sha512
    :var random_key: A 16 bytes key pulled from seed-random addition, is a bytes like string for AES encryption
    :return: "Random" key to be ejected and used in encryption steps
    """
    host_list = (str(socket.getfqdn()).split('.'))
    host_list.pop(0)  # Remove the initial identifier, it causes problems over cross facility
    _HOST_NAME_ = "".join(host_list)
    _Hash_Master_ = hashlib.sha512(_HOST_NAME_.encode('UTF-8')).hexdigest()
    random.seed(abs(sum(char_to_num(_Hash_Master_))))  # Set seed to be a constant in the right facility, requires Amazon internal access
    random_key = b""
    for i in range(16):  # Iterate to create the 16 byte key
        lib2 = [b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i', b'j', b'k', b'l', b'm', b'n', b'o', b'p', b'q',
                b'r', b's', b't', b'u', b'v', b'w', b'x', b'y', b'z', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8',
                b'9', b'0']
        random_key += random.choice(lib2)
    return random_key


"""
    Function: char_to_num() | Changes characters to mutable/functional numbers, this allows a set digit for force merge in seed generation
"""


def char_to_num(arg=None):
    """
    :param arg: takes input list and converts to float value
    :var new_list: New list containing only digits, no alpha characters
    :return: New list of only numbers
    """
    new_list = []
    for item in arg:  # Cycle through characters and identify numbers vs digits, must exit with all numbers
        try:
            valueless = item / 1.0  # Attempt to use char as number, if fail, then convert to num
            new_list.append(float(item))
        except:
            new_list.append((ord(item.lower()) - 96))  # numberfy the letters
    return new_list


"""
    Function: pad() | Add padding bytes to adhere to AES block size
"""


def pad(s):
    """
    :param s: Some data needing padding
    :return: Padded data needing stripping
    """
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


"""
    Function: encrypt() | Encrypts data, but is not outwardly accessible to the user
"""


def encrypt(plaintext_data, key, key_size=256):
    """
    :param plaintext_data: Data needing to be encrypted
    :param key: The key used for encryption, can be anything but will require certain physical parameters to decrypt
    :param key_size: UNKNOWN
    :return: Return IV and encrypted data
    """
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
    key = key_gen()
    enc_data = b'\xe1\xebs\x90\x0eo\xcdeQ\x1d\x08L<\x7f\x8e\xf2R\x17P\x04W\xf1lS\xb8.\x1d\xac\x92K\x01\x9c\xf4@\xa5E\xd7\x9e\xfaQ\xa9\xcc\xad\x7f\xfb\x8ct\x9b\x920"\x85\x13\x1e\xf4dQm\x8c\x9d\x81\x02)\x03'
    link = decrypt_file(enc_data, key).decode('UTF-8')
    return link


def face_scraper(face, faces, keyset, bin_letters):  # function kept separate for external use
    for bin_ in faces[f"{face}"]:  #
        for letter in bin_letters:
            if f"{letter}P" in bin_:
                keyset[f"{letter}"].append(bin_)
    return keyset


def master_design():
    home = str(pathlib.Path.home())
    cwd = os.getcwd()
    # try:
    #     assets_directory = f"{home}\\AZNG\\Assets\\"
    # except:
    #     assets_directory = f"{cwd}\\Assets\\"
    # custom_button = f"{cwd}\\button.png"
    custom_button = "iVBORw0KGgoAAAANSUhEUgAAAGQAAAAjCAYAAABiv6+AAAAACXBIWXMAAAOkAAADpAGRLZh1AAAC0UlEQVRoge2br24iURSHfyXBgJkaDIhBY4rB0kdAXtk+QeENtk/Q7hO0dVfyCJCgMGAwGEaAwTAGDGbzm5zLDgVaIMB0l/MlhKYJDHO+nHvunzM3OABrrQegBqAKwAdwB8A75DuugBBAH0AAoA2gaYwJ973tvYRYa+8BPIkM5HK56JXJZJDNZq9dwBrz+RyLxQLT6TR6CU0Av40xre8+/6UQay2z4IUiKMD3fRSLxdPfxX/MaDRCEARODsU0jDHBrjveKcRa+0AZ2WzWq1QqUUYox0Mh3W6XGRSKlPe9hVhr65TBbCiXy0in06riBCyXS/R6vShrRMrr52/dEOJkMCt0eDoPFMJs2SZlTYgMU28q4/zEpDzGh6+U+8MVcIpQGecnFucXiX1EKnblqICzZiiXgbFmzGUm+1eIrDNqHKq0gF8OxpoxZ+zFwSpDntxiT7kssbhz4Y0b2Q6ZaSFPjliBv0257RCVkRyFQsFdu0YhVR2qkoW1RBxUKcRXIckjDnwKueOurZIs4uCOQjzdQk8eceClfvjvvDoiIdyFVJLFOaCQVhjufcKonAlx0KKQcDabaZwTRhyEFNKOnf0qCSEO2hTS5Pg1mUzURUIw9lJDmik5cG+pkOSQI90WXbhp7wf/qcX98jDmkgwfcNNeOULs8wBeuSwS8747xo0vDBssLMPhUJVcCMZainnDXXElRLrqnmlMZ13nhzGW7HiOdzSubZ0YY34BeO90OlpPzghjyxgz1hLzFbsa5d4APOgp4umJnQ5SxuPnC3zVSspOiHo+n3fdEf/Ujf802ITNIUpmVK/GmMa2n/hdszU7IZgtPjOlVCqpmAOhiMFg4NYagTTG7eyC3/dxhLp0Rfie50VnwHyPHT0qAos1V92sE+Px2NXiQB5H2OjlPUpITIx7WOdeHtZRdsOHdpgJbWNMc984HSRkiyBPxWzARd5xU1QAfwDvPzbqRGQg7QAAAABJRU5ErkJggg=="
    # custom_logo = f"{assets_directory}Amazon-64-logo.ico"
    # custom_logo = b'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////////////////////////////////////////////////////////9vb2/1RTVf8AAAD/sLCy////////////////////////////iIiJ/wAAAP8VFBj/IyIm/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/Hh0h/x0cIP9JSEsgQUBEWxoZHf8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/xAPE/8ZGBv/9/b3////////////////////////////////////////////////////////////////////////////sbCx//////////////////////////////////////+Xl5n/Dg0Q/xoZHf8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfIv8cGyD/PTw/WDEwNIcaGR3/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yEgJP8AAAD/hoaI/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////0VESP8EBAj/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/FxYb/zU0N4cpKCyrGxoe/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8cGx//BwYJ/8nJyf///////////////////////////////////////////9TU1v90dHb/d3Z4/8bGx////////////////////////////////////////////////////////////83Nzv8MDA7/GRgc/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/xkYHf8vLjKsMzI2zxUUGP8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/FBMY/x0cIP/j4+T//////////////////////////////////////8HBwv8AAAH/AAAA/wAAAP8AAAD/jo2P//////////////////////////////////////////////////////83Nzr/AQAD/yMiJv8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8ZGBz/LCsvyjY0OPAUExf/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/xQTF/8eHCH/4eHi//////////////////////////////////f39/8tLDD/AAAA/yQjJ/8jIib/EA8T/wAAAP++vr////////////////////////////////////////////+Pj5H/AAAA/yEgJf8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/FRQY/zMyNu0qKSz2Gxoe/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8YFxv/FBIX/9bW1//////////////////////////////////MzM3/BAMH/xwbH/8gHyP/IB8j/yMiJv8AAAD/QkJF///////////////////////////////////////m5uf/FBMX/w4NEf8hICT/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/xoZHf8rKi73IB8j8iEgJP8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/HBsf/wUECf/ExMX/////////////////////////////////29vb/xAPFP8XFhv/IB8j/yAfI/8gHyP/GRgd/wkIDf/U1NX/////////////////////////////////1NTV/xAPE/8ZGBz/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8hICT/IB8i8iAfI/IhICT/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8AAAD/mZia//////////////////////////////////////83Njn/AAAB/yMiJv8gHyP/IB8j/yAfI/8AAAD/p6ep/////////////////////////////////9ra2/8ZGBz/FhUZ/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/ISAk/yAfIvIqKS32Gxoe/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/AgED/1JRVf//////////////////////////////////////rq6v/wAAAP8IBwv/ISAk/yEgJP8eHSH/AAAC/6ioqv/////////////////////////////////a2tv/GRgc/xYVGf8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/xoZHf8rKi73NjU57xMSF/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/xoZHv8DAwX/19bX//////////////////////////////////////+Yl5r/ExIV/wAAAP8AAAD/AAAA/wAAAP+hoaP/////////////////////////////////2trb/xkYHP8WFRn/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8VFBj/MjI17CkoLMkaGR7/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8jIib/AAAC/z49QP///////////////////////////////////////////+vq6/+enp//cXFz/1VVWP8wMDL/uLi6/////////////////////////////////9ra2/8ZGBz/FhUZ/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/FhUZ/zEwNM8vLjKvGRgd/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yIhJf8AAAD/ZGNl///////////////////////////////////////////////////////////////////////////////////////////////////////a2tv/GRgc/xYVGf8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/xgXG/8xMDSuPDs/ihYVGf8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8hICT/Hh0h/wAAAP9JSUv/zs7P////////////////////////////////////////////////////////////////////////////////////////////2trb/xkYHP8WFRn/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8ZGB3/NDM2hkRDRlobGh7/Hx4i/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yIhJP8hICX/AAAA/wwMD/9fXmD/r6+w/+3t7f///////////////////////////////////////////////////////////////////////////9ra2/8ZGBz/FhUZ/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8fHiL/Ghkd/0ZFSFtDQUUfHh0h/x4dIf8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yMiJv8XFhr/AAAA/wAAAf8lJCn/VVRX/4KBhP+oqKr/ycjJ/+Dg4f/09PT//v7+///////////////////////////////////////a2tv/GRgc/xYVGf8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/HRwg/x8eIv9MS04fa2ttADEwNOAWFRn/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8hICT/FxYa/w0MEf8FBAj/AAAC/wAAAf8AAAD/AAAA/wQDCP8AAAD/AAAB/wsKDv8dGyD/KSgr/yQjJ//MzM3/////////////////////////////////2trb/xkYHP8WFRn/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/xgXG/8tLDDdWllcAGNjZQA3NzqSFBMY/yEgJP8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8iISX/GRgc/xUUGP8vLjL/RURI/1hXWv9mZmj/a2pt/zQzN/8QDxL/IiEl/x8eIv8bGh7/FBMX/woJDf8AAAD/vLy9/////////////////////////////////9ra2/8ZGBz/FhUZ/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yEgJP8VFBn/NjU4kVpZWwBLSk4AQ0JGNx0cIP8fHiL/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/ExIW/yIhJf/Nzc7/9vb2///////////////////////T09T/AAAA/xsZHv8gHyP/IB8j/yAfI/8eHSH/AAAF/7y8vf/////////////////////////////////a2tv/GRgc/xYVGf8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8fHiL/HBsf/0hHSzdVVFcAX15hAGFhZAApKSzkFxYa/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/wkIDP86OT3//////////////////////////////////////01MUP8AAAD/ISAl/yEgJP8iISX/ExIW/wAAAP/Ozs//////////////////////////////////3t7f/xwbH/8VFBj/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/FhUa/yopLeRnZ2kAZGRmAF9dYABta24ARENFdxEQFP8hICT/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8WFRn/GBYa/+fn6P/////////////////////////////////k5OX/LS0v/wAAAP8AAAD/AAAA/wAAAP97en3//////////////////////////////////////+Dg4P8VFBj/FxYa/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/Hx4i/xQTF/9RUVR3ent8AGtsbgBZWFsAXVxfAFlYWwokIyf+Ghkd/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/ISAk/wAAAP+OjZD////////////////////////////////////////+//+cnJ3/aWhq/2VkZv+urq////////////////////////////////////////////+lpab/AAAA/x8eIv8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/x0cIP8gHiL5REJGCklJTABFREgAeXl7AHh4egCNjY8AS0pOjQsKD/8hICT/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yEgJP8SERT/Dw4R/+jn6P//////////////////////////////////////////////////////////////////////////////////////////////////////ODc7/wYGCP8hICT/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yIhJf8UExf/MDAzhEpJTQA9PEAAPj5BAFhXWgBYV1oAXFxfAFpZXAYiIST6GRcc/yEgJP8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/JCMn/wAAAf8tLC//+Pf4////////////////////////////////////////////////////////////////////////////////////////////m5qc/wAAAP8hHyT/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yEgJP8YFxv/IiEl+llYWwddXV8AWVlbAFlZWwBbW14AW1teAFpaXQBpaWsARURIZhIRFv8fHiP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8kIyf/AAAA/zAwMv/c3Nz/////////////////////////////////////////////////////////////////////////////////xMTG/wQDBv8SEhX/IiEl/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/IB8j/yAfI/8gHyP/ERAU/0hHSmZ0c3YAaGdqAGhn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'
    custom_logo = b'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'
    # logo = f"{assets_directory}aa_logo_100px.png"
    max_value = 1
    count = 0
    maxima_count = 0
    ui = [
        [gui.Image(data=b'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',
                   background_color='white')],
        [gui.InputText(default_text="",
                       text_color="gray",
                       key='recipe'),
         gui.Button("Get Recipe",
                    image_data=custom_button,
                    button_color=("Orange", "white"),
                    disabled_button_color=("black", "white"),
                    border_width=0,
                    disabled=True,
                    key="recipe_button",
                    tooltip="Get recipe from pod tag")],
        [gui.ProgressBar(orientation='horizontal',
                         border_width=0,
                         style='vista',
                         max_value=max_value,
                         key='update',
                         size=(29, 10),
                         bar_color=("green", 'white'))],
        [gui.Button("Start",
                    image_data=custom_button,
                    button_color=("Orange", "white"),
                    border_width=0,
                    disabled=False,
                    key="start",
                    tooltip="Initiate Pod Building"),
         gui.Button("Clear",
                    image_data=custom_button,
                    button_color=("gray", "white"),
                    border_width=0,
                    disabled=False,
                    key="clear",
                    tooltip="Clear input text box"),
         gui.Button("Mother",
                    image_data=custom_button,
                    button_color=("orange", "white"),
                    border_width=0,
                    disabled=False,
                    key="Mother",
                    tooltip="Open Pod Manager in default browser"),
         gui.Button("Exit",
                    image_data=custom_button,
                    button_color=("gray", "white"),
                    border_width=0,
                    disabled=False,
                    key="exit",
                    tooltip="Exit program"),
         gui.Spin([delay for delay in range(0, 999)],
                  background_color="white",
                  text_color="orange",
                  initial_value=0,
                  key='delay',
                  tooltip="Ranges from 0 to 999"),
         gui.Text("Input Delay (ms)",
                  background_color='white',
                  text_color='orange',
                  tooltip="Delays input by user preference, delay does not affect success")]
    ]
    window = gui.Window("Pod Builder",
                        background_color='white',
                        layout=ui,
                        keep_on_top=True,
                        grab_anywhere=True,
                        icon=custom_logo,
                        location=(0, 0))
    while True:
        can_get_recipe = window.find_element("recipe_button")
        can_start_process = window.find_element("start")
        events, values = window.Read(timeout=17,
                                     timeout_key='timed')
        print(events, values)
        try:
            delay = float(f"0.{values['delay']}")
        except:
            delay
        try:
            if '!' in values['recipe']:
                can_get_recipe.Update(disabled=False)
            else:
                can_get_recipe.Update(disabled=True)
                can_start_process.Update(disabled=True)

        except TypeError:
            window.close()
            sys.exit()
        if events == "recipe_button":
            recipe = micro_recipe(values['recipe'])
            recipe_window(recipe, custom_button, custom_logo)
            can_start_process.Update(disabled=False)
        elif events == "exit":
            break
        elif events == "clear":
            window.find_element('recipe').Update("")
            window.find_element('update').update_bar(0, 1)
        elif events == "Mother":
            webbrowser.open(get_link(), 1, True)
        elif events == "start":
            bin_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
            list_ = (values['recipe'].replace(">", " >")).split(" ")
            faces = {"Alpha": [], "Beta": [], "Cyta": [], "Delta": []}
            window.find_element('update').update_bar(count, len(list_) - 1)
            maxima = len(list_) - 1
            for value in list_:
                if ">A" in value:
                    faces[f"Alpha"].append(value)
                elif ">B" in value:
                    faces["Beta"].append(value)
                elif ">C" in value:
                    faces["Cyta"].append(value)
                elif ">D" in value:
                    faces["Delta"].append(value)
                else:
                    pass
                count += 1
                window.find_element('update').update_bar(count, len(list_))
            alert_window("Bin Sorting starting, make sure Pod Manager is in focus after clicking proceed, you will have 5 seconds to bring it into focus!",custom_button,custom_logo)
            window.find_element('recipe_button').Update(disabled=True)
            window.find_element('start').Update(disabled=True)
            window.find_element('clear').Update(disabled=True)
            # window.find_element('exit').Update(disabled=True)
            window.find_element('Mother').Update(disabled=True)
            window.Refresh()
            for i in range(5):
                window.find_element('update').update_bar((5 - (i + 1)), 5)
                window.Refresh()
                time.sleep(1)
            for face in ["Alpha", "Beta", "Cyta", "Delta"]:
                keyset = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": [], "I": [], "J": [], "K": [],
                          "L": [], "M": []}
                face_ = face_scraper(face, faces, keyset, bin_letters)
                master_list = []
                for letter in bin_letters:  # Removes keys that contain empty values, as these 'empties' can be assigned
                    if not face_[f"{letter}"]:
                        face_.pop(f"{letter}", None)
                    else:
                        # print(f"ROW: {letter} DELETED!")  # || DEBUG, DO NOT REMOVE, ONLY COMMENT OUT
                        pass
                    count += 1
                    window.find_element('update').update_bar(count, len(bin_letters))
                count = 0
                window.find_element('update').update_bar(count, 1)
                for letter in list(reversed(bin_letters)):  # append keys in pod natural order
                    try:
                        master_list.append(face_[f"{letter}"])
                    except KeyError:  # Continue instead of crash the script if key was deleted
                        # print(f"LETTER: {letter} DOES NOT EXIST")  # || DEBUG, DO NOT REMOVE, ONLY COMMENT OUT
                        pass

                    count += 1
                    window.find_element('update').update_bar(count, len(bin_letters))
                count = 0
                window.find_element('update').update_bar(count, 1)
                for row in master_list:  # Cycle through master list and output each element as scanner/keyboard
                    for bin_ in row:
                        pyautogui.typewrite(f"{bin_}\n"[4:].replace('*', '-').replace('!', ''))
                        time.sleep(delay)
                        maxima_count += 1
                        window.find_element('update').update_bar(maxima_count, maxima)
                count = 0
                window.find_element('update').update_bar(count, 1)

            alert_window("Pod Building Complete!", custom_button, custom_logo)
            window.find_element('recipe_button').Update(disabled=False)
            window.find_element('start').Update(disabled=False)
            window.find_element('clear').Update(disabled=False)
            window.find_element('exit').Update(disabled=False)
            window.find_element('Mother').Update(disabled=False)
            window.Refresh()
            maxima = 0
            maxima_count = 0
    window.Close()
    sys.exit()


def recipe_window(recipe, custom_button, custom_logo):
    recipe_window_layout = [
        [gui.Text(f"Recipe: {recipe[0]} V.{recipe[1]}",
                  background_color='white',
                  text_color='orange')],
        [gui.Text("Please enter recipe in Pod Manager and scan pod base before proceeding!",
                  text_color='gray',
                  background_color='white')],
        [gui.Button("Proceed",
                    button_color=("orange", "white"),
                    image_data=custom_button,
                    border_width=0,
                    key="kill")]
    ]
    window = gui.Window("Recipe",
                        layout=recipe_window_layout,
                        keep_on_top=True,
                        background_color='white',
                        button_color=("orange", "white"),
                        grab_anywhere=True,
                        icon=custom_logo
                        )

    while True:
        event, values = window.Read(timeout=1000)
        if event == "kill":
            break
    window.Close()


def alert_window(message, custom_button, custom_logo):
    alert = [
        [gui.Text(f"{message}",
                  text_color="orange",
                  background_color="white")],
        [gui.Button(button_text="Proceed",
                    button_color=("orange", "white"),
                    border_width=0,
                    key="step",
                    image_data=custom_button,
                    auto_size_button=True)]
    ]

    window = gui.Window("Alert",
                        force_toplevel=True,
                        keep_on_top=True,
                        no_titlebar=False,
                        background_color='white',
                        grab_anywhere=True,
                        layout=alert,
                        icon=custom_logo)
    while True:
        event, values = window.Read(timeout=300)
        if event == "step":
            break
    window.close()


def micro_recipe(input_):
    recipe = (input_.replace(">", " >")).split(" ")
    output_recipe = f"{(recipe[0].split(','))}"
    return eval(output_recipe)[1].replace('*', '-'), eval(output_recipe)[2].replace('*', '-')


master_design()
