import PySimpleGUI as gui
import pyautogui
import time
import sys
import webbrowser
from Encrypt import *

# Custom Button Image
custom_button = b"iVBORw0KGgoAAAANSUhEUgAAAGQAAAAjCAYAAABiv6+AAAAACXBIWXMAAAOkAAADpAGRLZh1AAAC0UlEQVRoge2br24iURSHfyXBgJkaDIhBY4rB0kdAXtk+QeENtk/Q7hO0dVfyCJCgMGAwGEaAwTAGDGbzm5zLDgVaIMB0l/MlhKYJDHO+nHvunzM3OABrrQegBqAKwAdwB8A75DuugBBAH0AAoA2gaYwJ973tvYRYa+8BPIkM5HK56JXJZJDNZq9dwBrz+RyLxQLT6TR6CU0Av40xre8+/6UQay2z4IUiKMD3fRSLxdPfxX/MaDRCEARODsU0jDHBrjveKcRa+0AZ2WzWq1QqUUYox0Mh3W6XGRSKlPe9hVhr65TBbCiXy0in06riBCyXS/R6vShrRMrr52/dEOJkMCt0eDoPFMJs2SZlTYgMU28q4/zEpDzGh6+U+8MVcIpQGecnFucXiX1EKnblqICzZiiXgbFmzGUm+1eIrDNqHKq0gF8OxpoxZ+zFwSpDntxiT7kssbhz4Y0b2Q6ZaSFPjliBv0257RCVkRyFQsFdu0YhVR2qkoW1RBxUKcRXIckjDnwKueOurZIs4uCOQjzdQk8eceClfvjvvDoiIdyFVJLFOaCQVhjufcKonAlx0KKQcDabaZwTRhyEFNKOnf0qCSEO2hTS5Pg1mUzURUIw9lJDmik5cG+pkOSQI90WXbhp7wf/qcX98jDmkgwfcNNeOULs8wBeuSwS8747xo0vDBssLMPhUJVcCMZainnDXXElRLrqnmlMZ13nhzGW7HiOdzSubZ0YY34BeO90OlpPzghjyxgz1hLzFbsa5d4APOgp4umJnQ5SxuPnC3zVSspOiHo+n3fdEf/Ujf802ITNIUpmVK/GmMa2n/hdszU7IZgtPjOlVCqpmAOhiMFg4NYagTTG7eyC3/dxhLp0Rfie50VnwHyPHT0qAos1V92sE+Px2NXiQB5H2OjlPUpITIx7WOdeHtZRdsOHdpgJbWNMc984HSRkiyBPxWzARd5xU1QAfwDvPzbqRGQg7QAAAABJRU5ErkJggg=="
# Custom logo for application
custom_logo = b'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'
_C_Mother_ = b'\xe1\xebs\x90\x0eo\xcdeQ\x1d\x08L<\x7f\x8e\xf2R\x17P\x04W\xf1lS\xb8.\x1d\xac\x92K\x01\x9c\xf4@\xa5E\xd7\x9e\xfaQ\xa9\xcc\xad\x7f\xfb\x8ct\x9b\x920"\x85\x13\x1e\xf4dQm\x8c\x9d\x81\x02)\x03'


def master_design():
    max_value = 1  # General default
    count = 0  # Count variable used in progress bars
    """
    ||| UI |||
    Master UI element that is the main user window. It is what should be interacted with most if the user is experienced.
    UI acts as only a layout to the window and does not process anything on its own. 
    
    Buttons have unique keys assigned to them that can be called from lower functions upon interaction or certain criteria.
    
    The recipe button allows a user to get the recipe from SAM2 card in a pod.
    
    The Start button starts the process of construction but only after a recipe is supplied via the SAM2 card.
    
    The Clear button clears the UI of its last completed recipe, the previous recipe is kept in the event a user made a
    mistake and must go back to rebuild the pod. 
    
    The Mother button calls to open the Mother program in the default browser, it will not be activated unless you are
    within the business network.
    
    The exit button simply exits the application.
    
    The text field is where a recipe can be scanned into. Recipe scanning takes a lot of time, and clicking off can lead
    to corruption of external environment.
    
    The delay spinner allows input of a delay number, this allows the "keyboard" input to be delayed, this is only for
    display purposes as the end result is the same, regardless of the interface feedback from Mother.
    
    The UI is themed orange and white per normal Amazon external theming.
    """
    ui = [
        [gui.Image(data=b'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',
                   background_color='white')],
        [gui.InputText(default_text="",
                       text_color="gray",
                       key='recipe',
                       enable_events=True),
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
                    tooltip="Initiate Pod Building",
                    enable_events=True),
         gui.Button("Clear",
                    image_data=custom_button,
                    button_color=("gray", "white"),
                    border_width=0,
                    disabled=False,
                    key="clear",
                    tooltip="Clear input text box",
                    enable_events=True),
         gui.Button("Mother",
                    image_data=custom_button,
                    button_color=("orange", "white"),
                    border_width=0,
                    disabled=False,
                    key="Mother",
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
    window = gui.Window("Pod Builder",
                        background_color='white',
                        layout=ui,
                        keep_on_top=True,
                        grab_anywhere=True,
                        icon=custom_logo,
                        location=(0, 0))
    while True:  # Keep reading window
        can_get_recipe = window.find_element("recipe_button")  # call back to Recipe button element for updating
        can_start_process = window.find_element("start")  # call back to Start button element for updating
        mother = window.find_element("Mother")  # call back to the Mother button for updating
        events, values = window.Read(timeout=500,
                                     timeout_key='timed')  # Read the textbox and button input every frame
        try:  # Attempt to decrypt mother URL, lock under failure
            mother.Update(disabled=True) if "http" not in get_link(enc_data=_C_Mother_) else window.find_element(
            "Mother").Update(disabled=False)
        except UnicodeDecodeError:  # Lock under ANY key failure
            mother.Update(disabled=True)
        print(events, values)
        delay = 0.0 if values['delay'] == '' else float(f"0.{values['delay']}")  # Set delay to a default in the event it is empty
        if values['recipe'].count('!') == 1 and '*' in values['recipe']:  # Make sure standard components of recipe are in word if possible
            can_get_recipe.Update(disabled=False)  # Enable button
        elif values['recipe'].count('!') > 1:  # Check if a second recipe has been scanned (no check for partial recipe
            alert_window(
                "WARNING: You may have entered more than 1 Recipe!\n\nRecipe will be cleared\n\nPlease scan after closing this window")
            # Alert user of bad input
            window.find_element('recipe').Update("")  # Auto clear recipe area
            window.find_element('update').update_bar(0, 1)  # Clear progress bar
        else:  # If failures have not occurred, enable recipe button
            can_get_recipe.Update(disabled=True)
            can_start_process.Update(disabled=True)
        if events == "recipe_button":  # Response to recipe button input
            recipe = micro_recipe(values['recipe'])  # Call micro recipe to return parsed recipe
            recipe_window(recipe, custom_button, custom_logo)  # Open a recipe window to reflect result
            can_start_process.Update(disabled=False)  # Enable start button
        elif events == "exit":  # Exit button response
            break  # Simply break out of the loop into exit
        elif events == "clear":  # Clear button response
            window.find_element('recipe').Update("")  # Clear recipe text bot
            window.find_element('update').update_bar(0, 1)  # Clear progress bar
            can_start_process.Update(disabled=True)
            can_get_recipe.Update(disabled=True)
            window.Refresh()
        elif events == "Mother":  # Mother response
            webbrowser.open(get_link(enc_data=_C_Mother_), 1, True)  # Decrypt and open link if possible
        elif events == "start":  # Start button response
            # Alert user of process start
            alert_window(
                "Bin Sorting starting, make sure Pod Manager is in focus after clicking proceed, you will have 5 seconds to bring it into focus!",
                custom_button, custom_logo)
            window.find_element('recipe_button').Update(disabled=True)  # Disable recipe button until done
            window.find_element('start').Update(disabled=True)  # Disable start button unitl done
            window.find_element('clear').Update(disabled=True)  # Disable clear until done
            window.find_element('Mother').Update(disabled=True)  # Disable Mother until done
            window.Refresh()  # Refresh window to reflect these changes immediately
            for i in range(5):  # Blocking countdown
                window.find_element('update').update_bar((5 - (i + 1)), 5)  # Update main window progress bar
                print(f"Update bar value: {5-i}")
                window.Refresh()  # Reflect changes manually
                time.sleep(1)  # Sleep countdown to per second
            base_list = values['recipe'][48:].replace('*', '-').strip('!').split('>')  # Recipe without header (BINS only)
            list_len = len(base_list)  # Number of bins to iterate over for progress bars

            new_dict = {"A": {},  # A-Face bins
                        "B": {},  # B-face bins
                        "C": {},  # C-face bins
                        "D": {}}  # D-Face bins

            for pod_bin in base_list:  # Iterate over all bins in the list to sort them
                if pod_bin.startswith('A'):  # If an A-face bin
                    new_dict["A"][f"{pod_bin[2]}"] = [] if pod_bin[2] not in new_dict["A"] else new_dict["A"][
                        f"{pod_bin[2]}"]  # Create key based on position in skirt
                    new_dict["A"][f"{pod_bin[2]}"].append(pod_bin[3:])  # Append bin to key value
                elif pod_bin.startswith('B'):  # If an B-face bin
                    new_dict["B"][f"{pod_bin[2]}"] = [] if pod_bin[2] not in new_dict["B"] else new_dict["B"][
                        f"{pod_bin[2]}"]  # Create key based on position in skirt
                    new_dict["B"][f"{pod_bin[2]}"].append(pod_bin[3:])  # Append bin to key value
                elif pod_bin.startswith('C'):  # If an C-face bin
                    new_dict["C"][f"{pod_bin[2]}"] = [] if pod_bin[2] not in new_dict["C"] else new_dict["C"][
                        f"{pod_bin[2]}"]  # Create key based on position in skirt
                    new_dict["C"][f"{pod_bin[2]}"].append(pod_bin[3:])  # Append bin to key value
                elif pod_bin.startswith('D'):  # If an D-face bin
                    new_dict["D"][f"{pod_bin[2]}"] = [] if pod_bin[2] not in new_dict["D"] else new_dict["D"][
                        f"{pod_bin[2]}"]  # Create key based on position in skirt
                    new_dict["D"][f"{pod_bin[2]}"].append(pod_bin[3:])  # Append bin to key value
                else:
                    pass
                count += 1  # Increment count for progress bar
                window.find_element('update').update_bar(count, list_len)  # Update progress bar to reflect status of sorting
            count = 0  # Reset counter
            for face, row in new_dict.items():  # Iterate over pod faces
                for level, bins in reversed(row.items()):  # Iterate over bins on face in build order
                    for pod_bin in bins:  # Output ordered bins into creation tool
                        print(f"Working Bin: {pod_bin}")
                        pyautogui.typewrite(f"{pod_bin}\n")  # Emulate scanner
                        time.sleep(delay)  # User input delay for display
                        count += 1  # Increment counter
                        window.find_element('update').update_bar(count, list_len)  # Update Progress bar
            alert_window("Pod Building Complete!", custom_button, custom_logo)  # Alert user of completion
            window.find_element('update').update_bar(0, 1)  # Reset progress bar
            window.find_element('recipe_button').Update(disabled=False)  # Enable recipe button
            window.find_element('start').Update(disabled=False)  # Enable start button
            window.find_element('clear').Update(disabled=False)  # Enable clear button
            window.find_element('exit').Update(disabled=False)  # Enable exit
            window.find_element('Mother').Update(disabled=False)  # Enable mother
            window.Refresh()  # Refresh window to reflect changes
            count = 0  # Reset counter
    window.Close()  # Close window process
    sys.exit()  # Kill script processes


def recipe_window(recipe, custom_button=custom_button, custom_logo=custom_logo):
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

    while True:  # Continue to refresh window to keep it alive
        event, values = window.Read(timeout=1000)
        if event == "kill":  # Kill process
            print("Recipe Window Killed")
            break
    window.Close()  # Kill window


def alert_window(message, custom_button=custom_button, custom_logo=custom_logo):
    """
    :param message: Message to relay to user upon certain criteria
    :param custom_button: Cutom button image
    :param custom_logo: Custom logo for the projects
    :return: None

    ||| UI |||
    Basic popup alert with custom message, allows for re-use without needing to make extra functions
    """
    alert = [
        [gui.Text(f"{message}",
                  text_color="orange",
                  background_color="white",
                  justification='center')],
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
    while True:  # Keep the window alive and refreshing
        event, values = window.Read(timeout=300)
        if event == "step":  # Kill the process with user input
            print("Alert Window Killed")
            break
    window.close()  # Clear up window


def micro_recipe(input_):
    """
    :param input_: User provided/scanned recipe
    :return: Recipe type and recipe version
    """
    recipe = (input_[:19].replace('*', '-')).split(",")  # Only parse through skin related header parts
    print("Recipe Filter")
    return recipe[1], recipe[2]  # Return the type and version string, ignoring card version


master_design()
