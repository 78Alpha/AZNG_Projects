import webbrowser as web
import PySimpleGUI as gui
import os

"""
:global: SetOptions: Sets the global theme to a light theme
:function: splash_screen(): Displays the company logo
:function: fc_menu(): The interactive, non blocking, non self destroying menu for associates
:function: icqa_load(): Prompts for login before launching ICQA Problem Solve related apps; details of apps in function
:function: afm_load(): Prompts for login before launching AFM Problem Solve toolset
:function: find_me(): Prompts for login and opens a guide to secondary app for scraping Bin labels
:function:
:function:
:return: Returns a closure to the window
"""

gui.SetOptions(use_ttk_buttons=True,  # Use native buttons
               ttk_theme="vista",  # Use Windows vista/windows native theme
               background_color="white",  # Sets global window BG color to white
               text_color="black",  # Sets global text to black
               element_background_color="white",  # Sets something to white, likely text boxes and stuff
               element_text_color="black",  # Lets element items like text boxes? Have colored (black) text
               input_text_color="black",  # Text input to text boxes have black text
               scrollbar_color="grey",  # Scroll bars will have a grey color
               input_elements_background_color="white"  # Elements that have input will have white backgrounds
               )

def splash_screen():
    """
    :gui: layout: This controls the physical layout; Should have a custom logo, no border, and auto-close
    :gui: window: The window display, auto terminates, can not be interacted with
    :return: No return
    """
    layout = [[gui.Image(f"{os.getcwd()}\\aa_logo.png")]]

    window = gui.Window(title="",  # Window title
                        no_titlebar=True,  # Removes titlebar
                        auto_close=True,  # Allows window to autoclose without user input
                        auto_close_duration=2,  # Time in seconds to keep window alive
                        force_toplevel=True,  # Forces window to always be on top of other windows
                        disable_minimize=True,  # Prevents user minimizing window
                        disable_close=True,  # prevents user closing window
                        layout=layout)
    window.read()

def icqa_load():
    """
    :function: web.open_new_tab(): Opens a new tab in the default browser given a URL
    :gui: lay_3: A gui layout for the login prompt, closes after button press
    :gui: win2: The window element to be interacted with
    :variable: input: The button input for the login prompt
    :variable: url_list: The list of URL's to actually open based on category
    """
    web.open_new_tab(FCMENU)

    lay_3 = [[gui.Text(text="Please login\n\n", background_color="white")],
             [gui.Text(text="Click the button when you are done", background_color="white")],
             [gui.Button(button_text="Logged In", size=(12, 1))]]

    win2 = gui.Window(no_titlebar=True,  # Removes title bar from window
                      title="",  # Window title
                      layout=lay_3,  # layout to use
                      auto_size_buttons=True,  # Automatically resize buttons if possible
                      auto_size_text=True,  # Aut-resize text if possible
                      keep_on_top=True,  # Keep window on top of others
                      grab_anywhere=True,  # Grab window anywhere to move it
                      element_justification="center"  # Centers all items
                      )
    input = win2.read()
    if input:
        win2.close()
    else:
        pass
    url_list = [FCResearch,  # FCResearch
                MoveItems,  # Move items, 1121
                PodConsole,  # Pod Console
                Rodeo,  # Rodeo
                Printmon,  # Printmon
                FC-ART,  # FC-ART
                TT]  # Trouble tickets
    for url in url_list:
        web.open_new_tab(url)

def afm_load():
    """
    :function: web.open_new_tab(): Opens a new tab in the default browser given a URL
    :gui: lay_3: A gui layout for the login prompt, notifies a kindle with MMA is required,closes after button press
    :gui: win2: The window element to be interacted with
    :variable: input: The button input for the login prompt
    :variable: url_list: The list of URL's to actually open based on category
    """
    web.open_new_tab(FCMENU)

    lay_3 = [[gui.Text(text="Please login\n\n", background_color="white")],
             [gui.Text(text="Make sure to grab a kindle with MMA if you have not done so!", text_color="red", background_color="white")],
             [gui.Text(text="Click the button when you are done", background_color="white")],
             [gui.Button(button_text="Logged In", size=(12, 1))]]

    win2 = gui.Window(no_titlebar=True,  # Removes title bar from window
                      title="",  # Window title
                      layout=lay_3,  # layout to use
                      auto_size_buttons=True,  # Automatically resize buttons if possible
                      auto_size_text=True,  # Aut-resize text if possible
                      keep_on_top=True,  # Keep window on top of others
                      grab_anywhere=True,  # Grab window anywhere to move it
                      element_justification="center"  # Centers all items
                      )
    input = win2.read()
    if input:
        win2.close()
    else:
        pass
    url_list = [PodConsole,  # Pod Console
                FCResearch,  # FCResearch
                MoveItems,  # Move items, 1121
                "Add_Back",  # Amnesty Addback tool
                "Routing",  # Tote Routing tool
                FC-ART,  # FC-ART
                TT]  # Trouble tickets
    for url in url_list:
        web.open_new_tab(url)

def find_me():
    """
        :function: web.open_new_tab(): Opens a new tab in the default browser given a URL
        :gui: lay_3: A gui layout for the login prompt, notifies a kindle with MMA is required,closes after button press
        :gui: win2: The window element to be interacted with
        :variable: input: The button input for the login prompt
        :variable: url_list: The list of URL's to actually open based on category
        """
    web.open_new_tab(FCMENU)

    lay_3 = [[gui.Text(text="Please login\n\n", background_color="white")],
             [gui.Text("Please read the BinScraper.txt instructions if you are new to BinScraper", text_color='red', background_color="white")],
             [gui.Text(text="Click the button when you are logged in", background_color="white")],
             [gui.Button(button_text="Logged In", size=(12, 1))]]

    win2 = gui.Window(no_titlebar=True,  # Removes title bar from window
                      title="",  # Window title
                      layout=lay_3,  # layout to use
                      auto_size_buttons=True,  # Automatically resize buttons if possible
                      auto_size_text=True,  # Aut-resize text if possible
                      keep_on_top=True,  # Keep window on top of others
                      grab_anywhere=True,  # Grab window anywhere to move it
                      element_justification="center"  # Centers all items
                      )
    input = win2.read()
    if input:
        win2.close()
    else:
        pass
    url_list = [FCResearch,  # FCResearch
                MoveItems,  # Move items, 1121
                FC-ART,  # FC-ART
                TT]  # Trouble tickets
    for url in url_list:
        web.open_new_tab(url)
    os.system(f"explorer.exe {os.getcwd()}\\BinScraper\\")
    os.system(f"start {os.getcwd()}\\BinScraper\\BinScraper.txt")

def pod_transfer():
    """
        :function: web.open_new_tab(): Opens a new tab in the default browser given a URL
        :gui: lay_3: A gui layout for the login prompt, notifies a kindle with MMA is required,closes after button press
        :gui: win2: The window element to be interacted with
        :variable: input: The button input for the login prompt
        :variable: url_list: The list of URL's to actually open based on category
        """
    web.open_new_tab(FCMENU)

    lay_3 = [[gui.Text(text="Please login\n\n", background_color="white")],
             [gui.Text(text="Click the button when you are logged in", background_color="white")],
             [gui.Button(button_text="Logged In", size=(12, 1))]]

    win2 = gui.Window(no_titlebar=True,  # Removes title bar from window
                      title="",  # Window title
                      layout=lay_3,  # layout to use
                      auto_size_buttons=True,  # Automatically resize buttons if possible
                      auto_size_text=True,  # Aut-resize text if possible
                      keep_on_top=True,  # Keep window on top of others
                      grab_anywhere=True,  # Grab window anywhere to move it
                      element_justification="center"  # Centers all items
                      )
    input = win2.read()
    if input:
        win2.close()
    else:
        pass
    url_list = [addPackage,  # Add Pod to Trailer
                DockOB,  # See logistics on Outbound trailers
                YardManager,  # Manage trailers currently in the yard
                DockIB,  # See logistics on Inbound trailers
                PodResearch,  # Research pod and automatically fix errors
                ServiceAudits]  # logs all worked on pods
    for url in url_list:
        web.open_new_tab(url)

def induct():
    """
        :function: web.open_new_tab(): Opens a new tab in the default browser given a URL
        :gui: lay_3: A gui layout for the login prompt, notifies a kindle with MMA is required,closes after button press
        :gui: win2: The window element to be interacted with
        :variable: input: The button input for the login prompt
        :variable: url_list: The list of URL's to actually open based on category
        """
    web.open_new_tab(FCMENU)

    lay_3 = [[gui.Text(text="Please login\n\n", background_color="white")],
             [gui.Text("A kindle with MMA is required! Make sure you have pallet jacks with H-frames.", text_color='red',
                       background_color="white")],
             [gui.Text(text="Click the button when you are logged in", background_color="white")],
             [gui.Button(button_text="Logged In", size=(12, 1))]]

    win2 = gui.Window(no_titlebar=True,  # Removes title bar from window
                      title="",  # Window title
                      layout=lay_3,  # layout to use
                      auto_size_buttons=True,  # Automatically resize buttons if possible
                      auto_size_text=True,  # Aut-resize text if possible
                      keep_on_top=True,  # Keep window on top of others
                      grab_anywhere=True,  # Grab window anywhere to move it
                      element_justification="center"  # Centers all items
                      )
    input = win2.read()
    if input:
        win2.close()
    else:
        pass
    url_list = # Mother, mastermind of the pods, for removal, building, and induct
    for url in url_list:
        web.open_new_tab(url)

def fc_menu():
    """
    :gui: layout: gui component, consists of custom logo, listbox displaying choices, submit and exit button
    :gui: window: The window component for the FC menu, forced to top level but can be overriden by calling top level
    :variable: button: Variable containing user button input, "LAUNCH!" or "EXIT"
    :variable: list_box: List of different operations to launch by role
    :variable: mode: Mode is the string containing the actual listbox output, extracting it from a key/list
    :gui: lay_2: Layout for the popup error message, blocking, not terminating, must display error message
    :gui: win: The window for the error message popup, forced to top overriding FC_MENU(), must be closed!
    :variable: input: reads the input from the error popup gui to ensure a user provided input, terminates popup
    """
    layout = [[gui.Image(f"{os.getcwd()}\\aa_logo_100px.png")],
              [gui.Listbox(values=["ICQA Problem Solve", "AFM Problem Solve", "Item Hunt", "Pod Transfer", "Induction"], size=(30, 10))],
              [gui.Button(button_text="LAUNCH!"), gui.Button(button_text="EXIT")]]

    window = gui.Window(title="AA Launcher", layout=layout, force_toplevel=True, keep_on_top=True)
    while True:
        button, list_box = window.read()
        try:
            mode = str(list_box[1][0])
        except:
            mode = ""
        if button == "LAUNCH!":
            if mode == "ICQA Problem Solve":
                icqa_load()
            elif mode == "AFM Problem Solve":
                afm_load()
            elif mode == "Item Hunt":
                find_me()
            elif mode == "Pod Transfer":
                pod_transfer()
            elif mode == "Induction":
                induct()
            else:
                lay_2 = [[gui.Text(text="PLEASE ENTER A SELECTION!", text_color="red", background_color="white")],
                         [gui.Button(button_text="ERROR", size=(7, 1))]]
                win = gui.Window(no_titlebar=True, title="", layout=lay_2, auto_size_buttons=True, auto_size_text=True, keep_on_top=True)
                input = win.read()
                if input:
                    win.close()
                else:
                    pass
        else:
            window.close()
            break



splash_screen()
fc_menu()
