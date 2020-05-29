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


def key_gen():
    host_list = (str(socket.getfqdn()).split('.'))
    host_list.pop(0)
    _HOST_NAME_ = "".join(host_list)
    _Hash_Master_ = hashlib.sha512(_HOST_NAME_.encode('UTF-8')).hexdigest()
    random.seed(abs(sum(char_to_num(_Hash_Master_))))
    random_key = b""
    for i in range(16):
        lib2 = [b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i', b'j', b'k', b'l', b'm', b'n', b'o', b'p', b'q',
                b'r', b's', b't', b'u', b'v', b'w', b'x', b'y', b'z', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8',
                b'9', b'0']
        random_key += random.choice(lib2)
    return random_key


def char_to_num(arg=None):
    new_list = []
    for item in arg:
        try:
            valueless = item / 1.0
            new_list.append(float(item))
        except:
            new_list.append((ord(item.lower()) - 96))
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
    assets_directory = f"{home}\\AZNG\\Assets\\"
    cwd = os.getcwd()
    # custom_button = f"{cwd}\\button.png"
    custom_button = "iVBORw0KGgoAAAANSUhEUgAAAGQAAAAjCAYAAABiv6+AAAAACXBIWXMAAAOkAAADpAGRLZh1AAAC0UlEQVRoge2br24iURSHfyXBgJkaDIhBY4rB0kdAXtk+QeENtk/Q7hO0dVfyCJCgMGAwGEaAwTAGDGbzm5zLDgVaIMB0l/MlhKYJDHO+nHvunzM3OABrrQegBqAKwAdwB8A75DuugBBAH0AAoA2gaYwJ973tvYRYa+8BPIkM5HK56JXJZJDNZq9dwBrz+RyLxQLT6TR6CU0Av40xre8+/6UQay2z4IUiKMD3fRSLxdPfxX/MaDRCEARODsU0jDHBrjveKcRa+0AZ2WzWq1QqUUYox0Mh3W6XGRSKlPe9hVhr65TBbCiXy0in06riBCyXS/R6vShrRMrr52/dEOJkMCt0eDoPFMJs2SZlTYgMU28q4/zEpDzGh6+U+8MVcIpQGecnFucXiX1EKnblqICzZiiXgbFmzGUm+1eIrDNqHKq0gF8OxpoxZ+zFwSpDntxiT7kssbhz4Y0b2Q6ZaSFPjliBv0257RCVkRyFQsFdu0YhVR2qkoW1RBxUKcRXIckjDnwKueOurZIs4uCOQjzdQk8eceClfvjvvDoiIdyFVJLFOaCQVhjufcKonAlx0KKQcDabaZwTRhyEFNKOnf0qCSEO2hTS5Pg1mUzURUIw9lJDmik5cG+pkOSQI90WXbhp7wf/qcX98jDmkgwfcNNeOULs8wBeuSwS8747xo0vDBssLMPhUJVcCMZainnDXXElRLrqnmlMZ13nhzGW7HiOdzSubZ0YY34BeO90OlpPzghjyxgz1hLzFbsa5d4APOgp4umJnQ5SxuPnC3zVSspOiHo+n3fdEf/Ujf802ITNIUpmVK/GmMa2n/hdszU7IZgtPjOlVCqpmAOhiMFg4NYagTTG7eyC3/dxhLp0Rfie50VnwHyPHT0qAos1V92sE+Px2NXiQB5H2OjlPUpITIx7WOdeHtZRdsOHdpgJbWNMc984HSRkiyBPxWzARd5xU1QAfwDvPzbqRGQg7QAAAABJRU5ErkJggg=="
    custom_logo = f"{assets_directory}Amazon-64-logo.ico"
    logo = f"{assets_directory}aa_logo_100px.png"
    max_value = 1
    count = 0
    maxima_count = 0
    ui = [
        [gui.Image(filename=logo,
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
