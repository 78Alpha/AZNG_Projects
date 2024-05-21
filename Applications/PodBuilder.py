import FreeSimpleGUI as gui
import pyautogui
import time
import sys
import webbrowser
try:
    from Encrypt import decrypt, decrypt_file, get_link  # Import necessary elements from Encrypt Module
except ModuleNotFoundError:
    print("Running without Encryption capabilities.")

version = "2.0.7"

# Custom Button Image
custom_button: bytes = b"iVBORw0KGgoAAAANSUhEUgAAAGQAAAAjCAYAAABiv6+AAAAACXBIWXMAAAOkAAADpAGRLZh1AAAC0UlEQVRoge2br24iURSHfyXBgJkaDIhBY4rB0kdAXtk+QeENtk/Q7hO0dVfyCJCgMGAwGEaAwTAGDGbzm5zLDgVaIMB0l/MlhKYJDHO+nHvunzM3OABrrQegBqAKwAdwB8A75DuugBBAH0AAoA2gaYwJ973tvYRYa+8BPIkM5HK56JXJZJDNZq9dwBrz+RyLxQLT6TR6CU0Av40xre8+/6UQay2z4IUiKMD3fRSLxdPfxX/MaDRCEARODsU0jDHBrjveKcRa+0AZ2WzWq1QqUUYox0Mh3W6XGRSKlPe9hVhr65TBbCiXy0in06riBCyXS/R6vShrRMrr52/dEOJkMCt0eDoPFMJs2SZlTYgMU28q4/zEpDzGh6+U+8MVcIpQGecnFucXiX1EKnblqICzZiiXgbFmzGUm+1eIrDNqHKq0gF8OxpoxZ+zFwSpDntxiT7kssbhz4Y0b2Q6ZaSFPjliBv0257RCVkRyFQsFdu0YhVR2qkoW1RBxUKcRXIckjDnwKueOurZIs4uCOQjzdQk8eceClfvjvvDoiIdyFVJLFOaCQVhjufcKonAlx0KKQcDabaZwTRhyEFNKOnf0qCSEO2hTS5Pg1mUzURUIw9lJDmik5cG+pkOSQI90WXbhp7wf/qcX98jDmkgwfcNNeOULs8wBeuSwS8747xo0vDBssLMPhUJVcCMZainnDXXElRLrqnmlMZ13nhzGW7HiOdzSubZ0YY34BeO90OlpPzghjyxgz1hLzFbsa5d4APOgp4umJnQ5SxuPnC3zVSspOiHo+n3fdEf/Ujf802ITNIUpmVK/GmMa2n/hdszU7IZgtPjOlVCqpmAOhiMFg4NYagTTG7eyC3/dxhLp0Rfie50VnwHyPHT0qAos1V92sE+Px2NXiQB5H2OjlPUpITIx7WOdeHtZRdsOHdpgJbWNMc984HSRkiyBPxWzARd5xU1QAfwDvPzbqRGQg7QAAAABJRU5ErkJggg=="
# Custom logo for application
custom_logo: bytes = b'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'

# Encrypted PodManager URL
_C_PodManager_: bytes = b'\xe1\xebs\x90\x0eo\xcdeQ\x1d\x08L<\x7f\x8e\xf2R\x17P\x04W\xf1lS\xb8.\x1d\xac\x92K\x01\x9c\xf4@\xa5E\xd7\x9e\xfaQ\xa9\xcc\xad\x7f\xfb\x8ct\x9b\x920"\x85\x13\x1e\xf4dQm\x8c\x9d\x81\x02)\x03'
# Pod builder logo
_C_POD_BUILDER_: bytes = b'iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAADl0lEQVR4nO3cv04UURiG8U/DJsRWIzEU01pgwVJhRbGtiQmNNyC34DVwCxgugcpSEkMDVLOFdDaS2GC0JZtgWBsWZZlZ5v935rzPr1RxJvmec2YzO4MZAAAA5DzyOvDV+fLU69ghGiQTl1k89jgowkEA4ghAHAGIIwBxS94nEJqfS89a/f+f//nV6v9fVnABtD0As/CG4IlLgDgCEEcA4ghAHAGIIwBxBCCOAMQRgDgCEEcA4ghAHAGIIwBxPBUcCJ4KhgsCEEcA4ghAHAGIIwBxBCCOAMQRgDgCEEcA4ng1rOPjh/ZaGjuAOAIQRwDiCEAcAYgjAHEEII4AxBGAOAIQRwDiCEAcAYgjAHEEII53AwPBu4FwQQDiCEAcAYgjAHEEII4AxBGAOAIQRwDiCEAc7wZ2fHzeDURQCECcewCb22v29feJ92nIcg1gkExsb++jmRkROHELYJBMLE3HXofHDa8ApvPDHw7XnU5Fm0cA94ZvZpamYxskE4fT0dZ1AJnDn0nTsa2u/jAzs4uLT12dk7QuH0RcOPw8KytvGj+REG8ERf9QaNUPfOwE7eosgOFw/bbwnZ33pX6WCNrj9l6AVbgkNHU54BLwj9t9gKvzZXaCALjeCTw5OCv9M0TQLNdXw+rc/n31dLPBs/EndwkwqzdEvjtohvu3gUTgyz0AMyLwFEQAR6fX9vLz28o/TwTVuQcwSCb2+vsLM7NaEaAa9wdCLneTO39WJQK+Sq7OLYCj0+t7w58pGwFfJVfn9kDIbNvPUycCPhMU53HzYetyN/lS5B8O3l3UGmafbhap3Aialhm+Wb+G2EddBrCVd82fNxv+zP8RFP0CiXCK6WrbmVYdfpbN7bXbx8mz9HH4MV8CKq/8PCcHZ7k7QR+H76nt6hpd+fPmPyD2efgx7gAMvwfaej288LZ/vLFv9i3770aj0YJVsW5pOp6a3X3eMESHh4cFfi3uqP0TydBGAIVX/vHGfq0DhT74Pmj6ElBu5cNdkwEUvsnz5MM5KzcQTQVQeOUz/LA08Rmg8DWf4Yen7g7Ayu+5OjsAKz8CVXcAhh+JKgGw7Uek7CWAlR+ZMjsAKz9CRXcAVn6kiuwArPyIPbQDsPIjt2gHYOULyNsBWPkisnYAhi8kK4BCQ2X4ccj8DPDQcBl+PHI/BOYNmeHHZeF9gPlhM/z4PHgjaDZ0hh+nQt8FMPx4uf+KGPgiAHEEAACApr98hyNlsb+5ggAAAABJRU5ErkJggg=='

Decryption_check = True

try:  # Attempt to decrypt PodManager URL, lock under failure
    if "http" not in get_link(enc_data=_C_PodManager_):
        print("Decrypt of link FAILED")
    else:
        Decryption_check = False
        print("Decrypt of link SUCCESS")
except:  # Lock under ANY key failure
    Decryption_check = True
    print("Link decryption FAILED")

size_ref: int = len("P-0-A000B000")


def master_design() -> None:
    max_value: int = 1  # General default
    count: int = 0  # Count variable used in progress bars
    """
    ||| UI |||
    Master UI element that is the main user window. It is what should be interacted with most if the user is experienced.
    UI acts as only a layout to the window and does not process anything on its own. 

    Buttons have unique keys assigned to them that can be called from lower functions upon interaction or certain criteria.

    The recipe button allows a user to get the recipe from SAM2 card in a pod.

    The Start button starts the process of construction but only after a recipe is supplied via the SAM2 card. Switched
    to "STOP" after frst pressed to allow for stopping mid-scan if an issue arrises.

    The Clear button clears the UI of its last completed recipe.

    The Pod Manager button calls to open the PodManager program in the default browser, it will not be activated unless you are
    within the business network.

    The exit button simply exits the application.

    The text field is where a recipe can be scanned into. Recipe scanning takes a lot of time, and clicking off can lead
    to corruption of external environment.

    The delay spinner allows input of a delay number, this allows the "keyboard" input to be delayed, this is only for
    display purposes as the end result is the same, regardless of the interface feedback from PodManager.

    The UI is themed orange and white per normal Amazon external theming.
    """
    ui: list = [
        [gui.InputText(default_text='',
                       text_color="gray",
                       key='recipe',
                       enable_events=True,
                       size=(70, 10)),
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
                         max_value=max_value,
                         key='update',
                         size=(45, 10),
                         bar_color=("green", 'lavender'))],
        [gui.Button("Start",
                    image_data=custom_button,
                    button_color=("Orange", "white"),
                    border_width=0,
                    disabled=True,
                    key="start",
                    tooltip="Start and Stop pod building",
                    enable_events=True),
         gui.Button("Reset",
                    image_data=custom_button,
                    button_color=("gray", "white"),
                    border_width=0,
                    disabled=False,
                    key="clear",
                    tooltip="Clear input text box",
                    enable_events=True),
         gui.Button("Pod Manager",
                    image_data=custom_button,
                    button_color=("orange", "white"),
                    border_width=0,
                    disabled=Decryption_check,
                    key="PodManager",
                    tooltip="Open Pod Manager in default browser",
                    enable_events=True),
         gui.Button("Exit",
                    image_data=custom_button,
                    button_color=("gray", "white"),
                    border_width=0,
                    disabled=False,
                    key="exit",
                    tooltip="Exit program",
                    enable_events=True),
         gui.Spin([delay for delay in range(0, 999)],
                  background_color="white",
                  text_color="orange",
                  size=(3, 3),
                  initial_value=0,
                  key='delay',
                  tooltip="Ranges from 0 to 999"),
         gui.Text("Input Delay (ms)",
                  background_color='white',
                  text_color='orange',
                  tooltip="Delays input by user preference, delay does not affect success")]
    ]
    window: gui.Window = gui.Window(f"Pod Builder {version}",
                                    background_color='white',
                                    layout=ui,
                                    keep_on_top=True,
                                    grab_anywhere=True,
                                    icon=_C_POD_BUILDER_,
                                    location=(0, 0))
    while True:  # Keep reading window
        can_get_recipe = window.find_element("recipe_button")  # call back to Recipe button element for updating
        can_start_process = window.find_element("start")  # call back to Start button element for updating
        PodManager = window.find_element("PodManager")  # call back to the PodManager button for updating
        events, values = window.Read(timeout_key='timed')  # Read the textbox and button input every frame
        window.find_element('start').Update(disabled=True)
        if events is gui.WINDOW_CLOSED:
            sys.exit()  # Exit whole thing instead of clsoing window and leaving loose threads
        try:  # Attempt to decrypt PodManager URL, lock under failure
            PodManager.Update(disabled=True) if "http" not in get_link(enc_data=_C_PodManager_) else window.find_element(
                "PodManager").Update(disabled=False)
            print("Decrypt of link SUCCESS")
        except:  # Lock under ANY key failure
            PodManager.Update(disabled=True)
            print("Link decryption FAILED")
        print(events, values)  # Debug, do not remove
        delay: float = 0.0 if values['delay'] == '' else float(f"0.{values['delay']}")  # Delay default if empty
        print(f"DELAY: {delay}")
        if values['recipe'].count('!') == 1 and '*' in values['recipe']:  # Is Part in Standard Recipe?
            can_get_recipe.Update(disabled=False)  # Enable button
        elif values['recipe'].count('!') > 1:  # Check if a second recipe has been scanned (no check for partial recipe
            alert_window("WARNING: You may have entered more than 1 Recipe!\n\nRecipe will be cleared\n\nPlease scan "
                         "after closing this window")
            # Alert user of bad input
            window.find_element('recipe').Update("")  # Auto clear recipe area
            window.find_element('update').update_bar(0, 1)  # Clear progress bar
        else:  # If failures have not occurred, enable recipe button
            can_get_recipe.Update(disabled=True)
            can_start_process.Update(disabled=True)
        if events == "recipe_button":  # Response to recipe button input
            recipe: tuple = micro_recipe(values['recipe'])  # Call micro recipe to return parsed recipe
            recipe_window(recipe)  # Open a recipe window to reflect result
            can_start_process.Update(disabled=False)  # Enable start button
        elif events == "exit":  # Exit button response
            break  # Simply break out of the loop into exit
        elif events == "clear":  # Clear button response
            window.find_element("recipe").Update(disabled=False)  # ALlow text input again
            window.find_element('recipe').Update("")  # Clear recipe text bot
            window.find_element('update').update_bar(0, 1)  # Clear progress bar
            can_start_process.Update(disabled=True)  # Allow user to start building again
            can_get_recipe.Update(disabled=True)  # Re-enable the recipe button in case user needs to reference it again
            window.Refresh()
        elif events == "PodManager":  # PodManager response
            webbrowser.open(get_link(enc_data=_C_PodManager_), 1, True)  # Decrypt and open link if possible
        elif events == "start":  # Start button response

            # Alert user of process start
            alert_window("Bring Pod Manager into focus before proceeding! DO not run with CAPS LOCK!")
            window.find_element('recipe_button').Update(disabled=True)  # Disable recipe button until done
            window.find_element('recipe').Update(disabled=True)
            window.find_element('start').Update("Stop", disabled=False)
            window.find_element('clear').Update(disabled=True)  # Disable clear until done
            window.find_element('PodManager').Update(disabled=True)  # Disable PodManager until done
            window.Refresh()  # Refresh window to reflect these changes immediately

            base_list: list = values['recipe'][48:].replace('*', '-').split('!')[0].split(
                '>')  # Recipe without header (BINS only)
            list_len: int = len(base_list)  # Number of bins to iterate over for progress bars

            new_dict: dict = {"A": {},  # A-Face bins
                              "B": {},  # B-face bins
                              "C": {},  # C-face bins
                              "D": {}}  # D-Face bins

            for pod_bin in base_list:  # Iterate over all bins in the list to sort them
                print(f"FACE: {pod_bin[0]}")
                print(f"LABEL: {pod_bin[2]}")
                new_dict[f"{pod_bin[0]}"][f"{pod_bin[2]}"] = [] if pod_bin[2] not in new_dict[f"{pod_bin[0]}"] else \
                    new_dict[f"{pod_bin[0]}"][f"{pod_bin[2]}"]  # Check dictionary for Face/Label/Bin
                new_dict[f"{pod_bin[0]}"][f"{pod_bin[2]}"].append(pod_bin[3:])  # Append bin to Face/Row
                count += 1  # Increment count for progress bar
                window.find_element('update').update_bar(count,
                                                         list_len)  # Update progress bar to reflect status of sorting
            count: int = 0  # Reset counter
            print(f"NEWDICT: {new_dict}")
            state_counter = False  # If set to true, will break out of the writing loop. Prevents ghost scans on restart.
            for face, row in new_dict.items():  # Iterate over pod faces
                for level, bins in reversed(row.items()):  # Iterate over bins on face in build order
                    for pod_bin in bins:  # Output ordered bins into creation tool
                        print(f"Working Bin: {(pod_bin.upper())[:size_ref]}")
                        temp_events, temp_values = window.Read(timeout=0)  # Force read the window at max speed to catch all input
                        if temp_events == "start":  # check for Stop and reset
                            window.find_element('update').update_bar(0, 1)  # Clear progress bar
                            window.find_element("start").Update("Start")  # Change 'Stop' button to 'Start' again
                            can_get_recipe.Update(disabled=True)  # Attempt to block text input to prevent new recipe
                            window.Refresh()  # reflect window changes
                            state_counter = True  # Set state counter to break in case it proceeds to a further event
                            return values['recipe']  # Return recipe to text input
                        if state_counter:  # Redundant catch
                            break
                        else:
                            pyautogui.typewrite(f"{(pod_bin.upper())[:size_ref]}\n", )  # Emulate scanner
                            time.sleep(delay)  # User input delay for display
                            count += 1  # Increment counter
                            window.find_element('update').update_bar(count, list_len)  # Update Progress bar
            alert_window("Pod Building Complete!")  # Alert user of completion
            window.find_element('update').update_bar(0, 1)  # Reset progress bar
            window.find_element('recipe_button').Update(disabled=False)  # Enable recipe button
            window.find_element('start').Update(disabled=False)  # Enable start button
            window.find_element('start').Update("Start")  # Change 'Stop' button to 'Start' after completion
            window.find_element('clear').Update(disabled=False)  # Enable clear button
            window.find_element('exit').Update(disabled=False)  # Enable exit
            window.find_element('PodManager').Update(disabled=False)  # Enable PodManager
            window.Refresh()  # Refresh window to reflect changes
            count: int = 0  # Reset counter
    window.Close()  # Close window process
    sys.exit()  # Kill script processes


def recipe_window(recipe: tuple) -> None:
    """
    :param recipe: The scanned Recipe to be used for processing
    :param custom_button: A user made button
    :param custom_logo: A custom logo for the projects
    :return: None
    ||| UI |||
    Recipe window layout is a basic popup window consisting of skin type and version as text with a continue button to
    exit the window safely.
    Themed to Amazon external spec
    """
    recipe_window_layout: list = [
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
    window: gui.Window = gui.Window("Recipe",
                                    layout=recipe_window_layout,
                                    keep_on_top=True,
                                    background_color='white',
                                    button_color=("orange", "white"),
                                    grab_anywhere=True,
                                    icon=custom_logo,
                                    disable_close=True
                                    )

    while True:  # Continue to refresh window to keep it alive
        event, values = window.Read(timeout=300)
        if event == "kill" or event == gui.WINDOW_CLOSED:  # Kill process
            print("Recipe Window Killed")
            break
    try:
        window.Close()  # Kill window
    except gui.WINDOW_CLOSED:
        pass


def alert_window(message: str) -> None:
    """
    :param message: Message to relay to user upon certain criteria
    :param custom_button: Cutom button image
    :param custom_logo: Custom logo for the projects
    :return: None
    ||| UI |||
    Basic popup alert with custom message, allows for re-use without needing to make extra functions
    """
    alert: list = [
        [gui.Text(f"{message}",
                  text_color="orange",
                  background_color="white",
                  justification='center')],
        [gui.Button(button_text="Proceed",
                    button_color=("orange", "white"),
                    border_width=0,
                    key="step",
                    image_data=custom_button,
                    auto_size_button=True,
                    enable_events=True)]
    ]

    window: gui.Window = gui.Window("Alert",
                                    keep_on_top=True,
                                    no_titlebar=False,
                                    background_color='white',
                                    grab_anywhere=True,
                                    layout=alert,
                                    icon=custom_logo,
                                    disable_close=True)
    window.Read()  # Read window, pauses before closure
    try:
        window.Close()  # Kill window
    except gui.WINDOW_CLOSED:
        pass


def micro_recipe(input_: str) -> tuple:
    """
    :param input_: User provided/scanned recipe
    :return: Recipe type and recipe version
    """
    recipe: list = (input_[:19].replace('*', '-')).split(",")  # Only parse through skin related header parts
    print("Recipe Filter")
    return recipe[1], recipe[2]  # Return the type and version string, ignoring card version


if __name__ == '__main__':
    while True:
        master_design()
