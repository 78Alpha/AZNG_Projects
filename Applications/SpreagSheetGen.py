import PySimpleGUI as gui
import os
import sys
import time

_C_VERSION: str = '1.0.5'

_C_ALPHABET_: list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # Alphabbet into list

_V_INIT_1_: int = 0  # Initial value for Spinner_1
_V_INIT_2_: int = 0  # Initial value for Spinner_2
_V_INIT_3_: int = 0  # Initial value for Spinner_3
_V_INIT_4_: int = 0  # Initial value for Spinner_4

_V_SLEEP_TIMER_: float = 0.2  # Delay between ticks of spinner objects, use feedback to determine good limit


def quad_check(value_1: int, value_2: int, value_3: int, value_4: int) -> None:
    """
    ||| Comparison |||

    This function is used to compare values returned from the gui and ensure they are in a usable integer format.
    Negative numbers would crash the range or produce a range on non-functional value.
    This will also check to make sure that the first counter in the range is not larger than the second counter as this
    would produce an inverted range, and that may not be the goal, and is currently out of scope for this script.

    :param value_1: Returned from gui as number value from spinner 1, used to determine range of bins
    :param value_2: Returned from gui as number value from spinner 1, used to determine range of bins
    :param value_3: Returned from gui as number value from spinner 1, used to determine range of bins
    :param value_4: Returned from gui as number value from spinner 1, used to determine range of bins
    :return: No value should be returned due to use of global variables
    """

    value_1 = 0 if int(value_1) <= 0 else int(value_1)  # force value to 0 if it would be negative
    value_2 = 0 if int(value_2) <= 0 else int(value_2)  # force value to 0 if it would be negative
    value_3 = 0 if int(value_3) <= 0 else int(value_3)  # force value to 0 if it would be negative
    value_4 = 0 if int(value_4) <= 0 else int(value_4)  # force value to 0 if it would be negative

    if value_2 < value_1:  # check if end of loop would be smaller than beginning and force them to be equal
        global _V_INIT_1_
        global _V_INIT_2_
        _V_INIT_2_ = value_1
        _V_INIT_1_ = _V_INIT_2_
    if value_4 < value_3:  # check if end of loop would be smaller than beginning and force them to be equal
        global _V_INIT_3_
        global _V_INIT_4_
        _V_INIT_4_ = value_3
        _V_INIT_3_ = _V_INIT_4_


def generate_csv(bin_array: list, file_name: str) -> None:
    """
    ||| Creation |||

    This function is meant to generate a csv file of the user's choice and write the created bins to the file for use
    in xml files and inventory.

    :param bin_array: A list of formatted bins to be put into a csv for later use in advanced xml files
    :param file_name: The saved directory for the file to be generated, this is input by the user from the gui
    :return: Nothing should be returned from this function
    """
    with open(file_name, 'w+') as csv_file:
        for formatted_bin in bin_array:
            csv_file.write(f"{formatted_bin}\n")


def generate_bins(data: dict, alphabet: list) -> list:
    """
    ||| Creation |||

    Takes the input that the user provided and returns a list of formatted string elements. The elements should return
    as A01-A-01 format for maximum compatibility. The alphabet is split to allow outputs to be within a selected range
    rather than all before and/or after a set character. This ruling also applies to numbers so that the start can be
    a non zero number. This allows flexibility but not inverted outputs.

    :param data: Data is returned as a dictionary from the gui and holds all info provided by the user
    :param alphabet: A list version of the alphabet used as a base for the iterated alphabet used in filtering, in scope
     placeholder
    :return: Returns a list of strings formatted to A01-A-01 format
    """
    letter_index: list = alphabet[alphabet.index(data["return_letter_2"]):alphabet.index(data["return_letter_3"]) + 1]
    _V_BIN_ARRAY_: list = []
    for cycle_1 in range(int(data['number_input_1']), int(data['number_input_2']) + 1):
        for letter in letter_index:
            for cycle_2 in range(int(data['number_input_3']), int(data['number_input_4']) + 1):
                formatted_string = f"{data['return_letter_1']}{cycle_1:02d}-{letter}-{cycle_2:02d}"
                _V_BIN_ARRAY_.append(formatted_string)
    return _V_BIN_ARRAY_


def main():
    """
    Globalizes the INIT variables, allows for mutability from all locations to allow for interop between all functions
    without having to point to the data and point back to save state. Must be careful with changing the values as they
    will mess with all other functions.
    """
    global _V_INIT_1_
    global _V_INIT_2_
    global _V_INIT_3_
    global _V_INIT_4_


    """
    Spinner object is a customized version of the spinner that does not rely on lists to show number values. This
    approach frees memory but cause partial misalignment with other gui elements. It is comprised of a read only text
    box to display numbers and to realtime buttons for fast and continuous input. Text input was disabled due to
    conflicts with windows refreshing. Each button has a key that can be referenced from the main window and used to
    force checks on values that may cause potential errors or reverse intent. This doc statement applies to all
    Spinner items.
    """
    Spinner_1 = [
        gui.Input('0', size=(5, 1), justification='r', key='number_input_1', readonly=True, enable_events=True, background_color='white', text_color='orange'),
        gui.RealtimeButton('▲', size=(1, 1), border_width=0,
                           button_color=(gui.theme_text_color('orange'), gui.theme_background_color('white')), key='input_1_up'),
        gui.RealtimeButton('▼', size=(1, 1), border_width=0,
                           button_color=(gui.theme_text_color(), gui.theme_background_color()),
                           key='input_1_down')
    ]

    Spinner_2 = [
        gui.Input('0', size=(5, 1), justification='r', key='number_input_2', readonly=True, enable_events=True, text_color='orange', background_color='white'),
        gui.RealtimeButton('▲', size=(1, 1), border_width=0,
                           button_color=(gui.theme_text_color(), gui.theme_background_color()), key='input_2_up'),
        gui.RealtimeButton('▼', size=(1, 1), border_width=0,
                           button_color=(gui.theme_text_color(), gui.theme_background_color()),
                           key='input_2_down')
    ]

    Spinner_3 = [
        gui.Input('0', size=(5, 1), justification='r', key='number_input_3', readonly=True, enable_events=True, text_color='orange', background_color='white'),
        gui.RealtimeButton('▲', size=(1, 1), border_width=0,
                           button_color=(gui.theme_text_color(), gui.theme_background_color()), key='input_3_up'),
        gui.RealtimeButton('▼', size=(1, 1), border_width=0,
                           button_color=(gui.theme_text_color(), gui.theme_background_color()),
                           key='input_3_down')
    ]

    Spinner_4 = [
        gui.Input('0', size=(5, 1), justification='r', key='number_input_4', readonly=True, enable_events=True, text_color='orange', background_color='white'),
        gui.RealtimeButton('▲', size=(1, 1), border_width=0,
                           button_color=(gui.theme_text_color(), gui.theme_background_color()), key='input_4_up'),
        gui.RealtimeButton('▼', size=(1, 1), border_width=0,
                           button_color=(gui.theme_text_color(), gui.theme_background_color()),
                           key='input_4_down')
    ]

    """
    Column elements are used to align the gui interface to calm the chaos that would result otherwise. The eye should
    follow the visual elements in a slight rolling motion to improve interest in each element but not have a harsh
    method of display that would cause confusion of element purpose. This doc is to reflect on the purpose of the
    columns but not what each on is being used for.
    """


    """
    Column 1 is a letter selection dropdown menu. This is used to determine the single start character of the formatted
    strings. The only active elements is the dropdown menu, with text on top used to show an example letter and the
    ending text is used solely as vertical buffer.
    """

    column_1 = [
        [gui.Text(_C_ALPHABET_[0], size=(2, 1), key="display_letter_1", background_color='white', text_color='green', font=('Helvetica', 12, 'bold'))],
        [gui.DropDown(_C_ALPHABET_, default_value=_C_ALPHABET_[0], size=(2, 1), key="return_letter_1",
                      enable_events=True, readonly=True, background_color='white', text_color='orange')],
        [gui.Text(background_color='white')]
    ]

    """
    Column 2 uses the Spinner_1 and the Spinner_2 custom elements to determine the ranges of numbers in bins. The text
    example for this range is in a buffered integer-string format, such that all numbers will be 01-09 if less than 10
    or their number, should they be greater.
    """

    column_2 = [
        [gui.Text(f"{_V_INIT_2_:02d}", size=(5, 1), key="display_number_1", background_color='white', text_color='green', font=('Helvetica', 12, 'bold'))],
        Spinner_1,
        Spinner_2,
    ]

    """
    A dash elements with vertical text buffers to allow a smooth and matching theme
    """

    column_3 = [
        [gui.Text("-", size=(1, 1), background_color='white', text_color='green', font=('Helvetica', 12, 'bold'))],
        [gui.Text(background_color='white')],
        [gui.Text(background_color='white')]
    ]

    """
    Column_4 is a letter range selection. It used 2 dropdown menus that select a target and run checks to ensure a
    letter selected for the start does not exceed a letter in the end, this disallows reverse letter lists. This element
    used the legacy lists method but should be kept this way to allow for slicing. The text field is to give an example
    of a letter. The elements have keys that are read from directly but should not be altered aside from comparison and
    corrections.
    """

    column_4 = [
        [gui.Text(_C_ALPHABET_[0], size=(2, 1), key="display_letter_2", background_color='white', text_color='green', font=('Helvetica', 12, 'bold'))],
        [gui.DropDown(_C_ALPHABET_, default_value=_C_ALPHABET_[0], size=(2, 1), key="return_letter_2",
                      enable_events=True, readonly=True, background_color='white', text_color='orange')],
        [gui.DropDown(_C_ALPHABET_, default_value=_C_ALPHABET_[0], size=(2, 1), key="return_letter_3",
                      enable_events=True, readonly=True, background_color='white', text_color='orange')],
    ]

    """
    A buffered dash that allows the gui to appear more fluidly
    """

    column_5 = [
        [gui.Text("-", size=(1, 1), background_color='white', text_color='green', font=('Helvetica', 12, 'bold'))],
        [gui.Text(background_color='white')],
        [gui.Text(background_color='white')]
    ]

    """
    Used the remaining spinner elements to determing the trailing range of numbers for formatting. It also uses the
    buffered integer-string format 01-09 if the integer is less than 10 or the number itself if greater. They will
    not allow the second number to be smaller than the initial range. As with the earlier, there are checks in place
    to prohibit reverse ranges.
    """

    column_6 = [
        [gui.Text(f"{_V_INIT_4_:02d}", size=(5, 1), key="display_number_2", background_color='white', text_color='green', font=('Helvetica', 12, 'bold'))],
        Spinner_3,
        Spinner_4,
    ]

    """
    The main gui layout, this shows the version, an example of what the layout should look like once generated, all the
    column elements, and a save as button. The save as button returns a file name and the path to the file. This allows
    for multiple files to be saved, a better solution than writing to the same file that will have permission errors.
    """

    main_layout = [
        [gui.Text(f"SpreadSheetGen V.{_C_VERSION}", text_color='orange', font=('Helvetica', 20, 'bold'), background_color='white')],
        [gui.Text("EXAMPLE:", text_color='green', background_color='white', font=('Helvetica', 12, 'bold')), gui.Text("A01-A-01", key="example", background_color='white', text_color='orange', font=('Helvetica', 12, 'bold'))],
        [gui.Column(column_1, background_color='white'),
         gui.Column(column_2, background_color='white'),
         gui.Column(column_3, background_color='white'),
         gui.Column(column_4, background_color='white'),
         gui.Column(column_5, background_color='white'),
         gui.Column(column_6, background_color='white')],
        [gui.SaveAs("Export", button_color=('orange', 'white'), file_types=(("CSV", "*.csv"), ("All Files", "*.*")), key="save_as", enable_events=True)],
    ]

    main_window = gui.Window("SpreadSheetGen", main_layout, background_color='white', titlebar_background_color='white',)

    while True:
        events, values = main_window.Read()  # read the events (button presses) and values (values returned by elements)
        if events is None:  # If gui window closed but functions left running, close the gui and force terminate
            main_window.close()
            sys.exit()
        if events == "input_1_up":  # Up button pressed on Spinner_1
            _V_INIT_1_ += 1  # add 1
            if _V_INIT_1_ >= _V_INIT_2_:  # if the start of range is larger than the end of range
                _V_INIT_2_ = _V_INIT_1_  # make ranges equal
                main_window.find_element("number_input_2").update(_V_INIT_2_)  # show new value of end range in gui
            main_window.find_element("number_input_1").update(_V_INIT_1_)  # show new value of start range in gui
            main_window.Refresh()  # Refresh gui to show new values
            time.sleep(_V_SLEEP_TIMER_)  # wait the hard coded time between realtime button inputs
        elif events == "input_1_down":  # Down button on Spinner_1
            _V_INIT_1_ -= 1  # subtract 1
            if _V_INIT_1_ <= 0:  # If value is negative
                _V_INIT_1_ = 0  # make it 0
            if _V_INIT_1_ >= _V_INIT_2_:  # is the value of the start is greater than or equal to end range
                _V_INIT_2_ = _V_INIT_1_  # make them equal
                main_window.find_element("number_input_2").update(_V_INIT_2_)  # update end range value
            main_window.find_element("number_input_1").update(_V_INIT_1_)  # update start range value
            main_window.Refresh()  # show new values in gui
            time.sleep(_V_SLEEP_TIMER_)  # wait hard coded time between realtime button presses
        if events == "input_2_up":  # Spinner_2 up button pressed
            _V_INIT_2_ += 1  # add 1
            main_window.find_element("number_input_2").update(_V_INIT_2_)  # update value
            main_window.Refresh()  # show value in gui
            time.sleep(_V_SLEEP_TIMER_)  # wait hard coded time in between realtime button presses
        elif events == "input_2_down":  # Spinner_2 button down
            _V_INIT_2_ -= 1  # subtract 1
            if _V_INIT_2_ <= 0:  # if negative
                _V_INIT_2_ = 0  # make 0
            if _V_INIT_2_ < _V_INIT_1_:  # if less than start range
                _V_INIT_1_ = _V_INIT_2_  # make ranges equal
                main_window.find_element('number_input_1').update(_V_INIT_1_)  # update start range value
            main_window.find_element("number_input_2").update(_V_INIT_2_)  # update end range value
            main_window.Refresh()  # show new values in gui
            time.sleep(_V_SLEEP_TIMER_)  # wait hard coded time between realtime button presses
        if events == "return_letter_2":  # If start range letter dropdown pressed/changed
            if _C_ALPHABET_.index(values["return_letter_2"]) >= _C_ALPHABET_.index(values["return_letter_3"]):  # if start range letter comes after end range letter
                try:  # attempt to make end range letter 1 more than start range
                    main_window.find_element("return_letter_3").update(_C_ALPHABET_[_C_ALPHABET_.index(values["return_letter_2"]) + 1])
                except IndexError:  # make start range 1 letter less if at Z
                    main_window.find_element("return_letter_3").update(_C_ALPHABET_[-1])
        if events == "return_letter_3":  # if dropdown menu for end letter range pressed/changed
            if _C_ALPHABET_.index(values["return_letter_3"]) <= _C_ALPHABET_.index(values["return_letter_2"]):  # if letter is before start range
                try:  # make start range 1 less than end range
                    main_window.find_element("return_letter_2").update(_C_ALPHABET_[_C_ALPHABET_.index(values["return_letter_3"]) - 1])
                except IndexError:  # make start range "A" if failed
                    main_window.find_element("return_letter_2").update(_C_ALPHABET_[0])
        if events == "input_3_up":
            _V_INIT_3_ += 1
            if _V_INIT_3_ >= _V_INIT_4_:
                _V_INIT_4_ = _V_INIT_3_
                main_window.find_element("number_input_4").update(_V_INIT_4_)
            main_window.find_element("number_input_3").update(_V_INIT_3_)
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        elif events == "input_3_down":
            _V_INIT_3_ -= 1
            if _V_INIT_3_ <= 0:
                _V_INIT_3_ = 0
            if _V_INIT_3_ >= _V_INIT_4_:
                _V_INIT_4_ = _V_INIT_3_
                main_window.find_element("number_input_4").update(_V_INIT_4_)
            main_window.find_element("number_input_3").update(_V_INIT_3_)
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        if events == "input_4_up":
            _V_INIT_4_ += 1
            main_window.find_element("number_input_4").update(_V_INIT_4_)
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        elif events == "input_4_down":
            _V_INIT_4_ -= 1
            if _V_INIT_4_ <= 0:
                _V_INIT_4_ = 0
            if _V_INIT_4_ < _V_INIT_3_:
                _V_INIT_3_ = _V_INIT_4_
                main_window.find_element('number_input_3').update(_V_INIT_3_)
            main_window.find_element("number_input_4").update(_V_INIT_4_)
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        if events == "save_as":
            quad_check(values['number_input_1'], values['number_input_2'], values['number_input_3'], values['number_input_4'])
            main_window.find_element('number_input_1').Update(int(values['number_input_1']))
            main_window.find_element('number_input_2').Update(int(values['number_input_2']))
            main_window.find_element('number_input_3').Update(int(values['number_input_3']))
            main_window.find_element('number_input_4').Update(int(values['number_input_4']))
            main_window.Refresh()
            save_file = values["save_as"]
            bin_array = generate_bins(values, _C_ALPHABET_)
            generate_csv(bin_array=bin_array, file_name=save_file)
        print(events, values)
    pass


if __name__ == '__main__':
    main()
