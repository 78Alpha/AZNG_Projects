import PySimpleGUI as gui
import os
import sys
import time

_C_VERSION: str = '1.0.4'

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

    value_1 = 0 if value_1 <= 0 else value_1  # force value to 0 if it would be negative
    value_2 = 0 if value_2 <= 0 else value_2  # force value to 0 if it would be negative
    value_3 = 0 if value_3 <= 0 else value_3  # force value to 0 if it would be negative
    value_4 = 0 if value_4 <= 0 else value_4  # force value to 0 if it would be negative

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
    letter_index: list = alphabet[alphabet.index(data["return_letter_2"]):alphabet.index(data["return_letter_3"]) + 1]
    _V_BIN_ARRAY_: list = []
    for cycle_1 in range(int(data['number_input_1']), int(data['number_input_2']) + 1):
        for letter in letter_index:
            for cycle_2 in range(int(data['number_input_3']), int(data['number_input_4']) + 1):
                formatted_string = f"{data['return_letter_1']}{cycle_1:02d}-{letter}-{cycle_2:02d}"
                _V_BIN_ARRAY_.append(formatted_string)
    return _V_BIN_ARRAY_


def main():
    global _V_INIT_1_
    global _V_INIT_2_
    global _V_INIT_3_
    global _V_INIT_4_

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

    column_1 = [
        [gui.Text(_C_ALPHABET_[0], size=(2, 1), key="display_letter_1", background_color='white', text_color='green', font=('Helvetica', 12, 'bold'))],
        [gui.DropDown(_C_ALPHABET_, default_value=_C_ALPHABET_[0], size=(2, 1), key="return_letter_1",
                      enable_events=True, readonly=True, background_color='white', text_color='orange')],
        [gui.Text(background_color='white')]
    ]

    column_2 = [
        [gui.Text(f"{_V_INIT_2_:02d}", size=(5, 1), key="display_number_1", background_color='white', text_color='green', font=('Helvetica', 12, 'bold'))],
        Spinner_1,
        Spinner_2,
    ]

    column_3 = [
        [gui.Text("-", size=(1, 1), background_color='white', text_color='green', font=('Helvetica', 12, 'bold'))],
        [gui.Text(background_color='white')],
        [gui.Text(background_color='white')]
    ]

    column_4 = [
        [gui.Text(_C_ALPHABET_[0], size=(2, 1), key="display_letter_2", background_color='white', text_color='green', font=('Helvetica', 12, 'bold'))],
        [gui.DropDown(_C_ALPHABET_, default_value=_C_ALPHABET_[0], size=(2, 1), key="return_letter_2",
                      enable_events=True, readonly=True, background_color='white', text_color='orange')],
        [gui.DropDown(_C_ALPHABET_, default_value=_C_ALPHABET_[0], size=(2, 1), key="return_letter_3",
                      enable_events=True, readonly=True, background_color='white', text_color='orange')],
    ]

    column_5 = [
        [gui.Text("-", size=(1, 1), background_color='white', text_color='green', font=('Helvetica', 12, 'bold'))],
        [gui.Text(background_color='white')],
        [gui.Text(background_color='white')]
    ]

    column_6 = [
        [gui.Text(f"{_V_INIT_4_:02d}", size=(5, 1), key="display_number_2", background_color='white', text_color='green', font=('Helvetica', 12, 'bold'))],
        Spinner_3,
        Spinner_4,
    ]

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

    _C_SPIN_KEYS_1_UP_ = ["input_1_up", "input_2_up"]
    _C_SPIN_KEYS_2_UP_ = ["input_3_up", "input_4_up"]
    _C_SPIN_KEYS_1_DOWN_ = ["input_1_down", "input_2_down"]
    _C_SPIN_KEYS_2_DOWN_ = ["input_3_down", "input_4_down"]
    _C_SPIN_SHOW_1_ = ["number_input_1", "number_input_2"]
    _C_SPIN_SHOW_2_ = ["number_input_3", "number_input_4"]
    _C_V_INIT_1_ = [_V_INIT_1_, _V_INIT_2_]
    _C_V_INIT_2_ = [_V_INIT_3_, _V_INIT_4_]

    main_window = gui.Window("SpreadSheetGen", main_layout, background_color='white', titlebar_background_color='white',)

    while True:
        events, values = main_window.Read()
        if events is None:
            main_window.close()
            sys.exit()
        if events == "input_1_up":
            _V_INIT_1_ += 1
            if _V_INIT_1_ >= _V_INIT_2_:
                _V_INIT_2_ = _V_INIT_1_
                main_window.find_element("number_input_2").update(_V_INIT_2_)
            main_window.find_element("number_input_1").update(_V_INIT_1_)
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        elif events == "input_1_down":
            _V_INIT_1_ -= 1
            if _V_INIT_1_ <= 0:
                _V_INIT_1_ = 0
            if _V_INIT_1_ >= _V_INIT_2_:
                _V_INIT_2_ = _V_INIT_1_
                main_window.find_element("number_input_2").update(_V_INIT_2_)
            main_window.find_element("number_input_1").update(_V_INIT_1_)
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        if events == "input_2_up":
            _V_INIT_2_ += 1
            main_window.find_element("number_input_2").update(_V_INIT_2_)
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        elif events == "input_2_down":
            _V_INIT_2_ -= 1
            if _V_INIT_2_ <= 0:
                _V_INIT_2_ = 0
            if _V_INIT_2_ < _V_INIT_1_:
                _V_INIT_1_ = _V_INIT_2_
                main_window.find_element('number_input_1').update(_V_INIT_1_)
            main_window.find_element("number_input_2").update(_V_INIT_2_)
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        if events == "return_letter_2":
            if _C_ALPHABET_.index(values["return_letter_2"]) >= _C_ALPHABET_.index(values["return_letter_3"]):
                try:
                    main_window.find_element("return_letter_3").update(_C_ALPHABET_[_C_ALPHABET_.index(values["return_letter_2"]) + 1])
                except IndexError:
                    main_window.find_element("return_letter_3").update(_C_ALPHABET_[-1])
        if events == "return_letter_3":
            if _C_ALPHABET_.index(values["return_letter_3"]) <= _C_ALPHABET_.index(values["return_letter_2"]):
                try:
                    main_window.find_element("return_letter_2").update(_C_ALPHABET_[_C_ALPHABET_.index(values["return_letter_3"]) - 1])
                except IndexError:
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
            main_window.find_element('number_input_2').Update(int(values['number_input_1']))
            main_window.find_element('number_input_3').Update(int(values['number_input_3']))
            main_window.find_element('number_input_4').Update(int(values['number_input_3']))
            main_window.Refresh()
            save_file = values["save_as"]
            bin_array = generate_bins(values, _C_ALPHABET_)
            generate_csv(bin_array=bin_array, file_name=save_file)
        print(events, values)
    pass


if __name__ == '__main__':
    main()
