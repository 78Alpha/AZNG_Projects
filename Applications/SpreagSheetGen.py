import PySimpleGUI as gui
import os
import sys
import time

_C_VERSION = '1.0.2'

_C_ALPHABET_ = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
_V_INIT_1_ = [0, 1]
_V_INIT_2_ = [0, 1]
_V_INIT_3_ = [0, 1]
_V_INIT_4_ = [0, 1]

_V_SLEEP_TIMER_ = 0.2


def quad_check(value_1, value_2, value_3, value_4):
    value_1 = int(value_1)
    value_2 = int(value_2)
    value_3 = int(value_3)
    value_4 = int(value_4)
    if value_2 < value_1:
        global _V_INIT_1_
        global _V_INIT_2_
        for i in range(value_2):
            _V_INIT_2_ = []
            _V_INIT_2_.append(i)
        _V_INIT_1_ = _V_INIT_2_
    if value_4 < value_3:
        global _V_INIT_3_
        global _V_INIT_4_
        for i in range(value_4):
            _V_INIT_4_ = []
            _V_INIT_4_.append(i)
        _V_INIT_3_ = _V_INIT_4_


def list_set_1_add():
    global _V_INIT_1_
    global _V_INIT_2_
    _V_INIT_1_.append(_V_INIT_1_[-1] + 1)
    _V_INIT_2_.append(_V_INIT_2_[-1] + 1)


def list_set_2_add():
    global _V_INIT_3_
    global _V_INIT_4_
    _V_INIT_3_.append(_V_INIT_3_[-1] + 1)
    _V_INIT_4_.append(_V_INIT_4_[-1] + 1)


def list_set_1_remove():
    global _V_INIT_1_
    global _V_INIT_2_
    _V_INIT_1_.pop(-1)
    _V_INIT_2_.pop(-1)


def list_set_2_remove():
    global _V_INIT_3_
    global _V_INIT_4_
    _V_INIT_3_.pop(-1)
    _V_INIT_4_.pop(-1)


def list_set_1_gen(data_range):
    global _V_INIT_1_
    global _V_INIT_2_
    _V_INIT_1_ = []
    _V_INIT_2_ = []
    for i in range(int(data_range)):
        _V_INIT_1_.append(i)
        _V_INIT_2_.append(i)
    # _V_INIT_2_.append(int(_V_INIT_1_[-1])+1)


def list_set_2_gen(data_range):
    global _V_INIT_3_
    global _V_INIT_4_
    _V_INIT_3_ = []
    _V_INIT_4_ = []
    for i in range(int(data_range)):
        _V_INIT_3_.append(i)
        _V_INIT_4_.append(i)
    # _V_INIT_4_.append(int(_V_INIT_3_[-1])+1)


def generate_csv(bin_array, file_name):
    with open(file_name, 'w+') as csv_file:
        for formatted_bin in bin_array:
            csv_file.write(f"{formatted_bin}\n")
    pass


def generate_bins(data, alphabet):
    letter_index = alphabet[alphabet.index(data["return_letter_2"]):alphabet.index(data["return_letter_3"]) + 1]
    _V_BIN_ARRAY_ = []
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
        gui.Input('0', size=(5, 1), justification='r', key='number_input_1', enable_events=True, background_color='white', text_color='orange'),
        gui.RealtimeButton('▲', size=(1, 1), border_width=0,
                           button_color=(gui.theme_text_color('orange'), gui.theme_background_color('white')), key='input_1_up'),
        gui.RealtimeButton('▼', size=(1, 1), border_width=0,
                           button_color=(gui.theme_text_color(), gui.theme_background_color()),
                           key='input_1_down')
    ]

    Spinner_2 = [
        gui.Input('0', size=(5, 1), justification='r', key='number_input_2', enable_events=True, text_color='orange', background_color='white'),
        gui.RealtimeButton('▲', size=(1, 1), border_width=0,
                           button_color=(gui.theme_text_color(), gui.theme_background_color()), key='input_2_up'),
        gui.RealtimeButton('▼', size=(1, 1), border_width=0,
                           button_color=(gui.theme_text_color(), gui.theme_background_color()),
                           key='input_2_down')
    ]

    Spinner_3 = [
        gui.Input('0', size=(5, 1), justification='r', key='number_input_3', enable_events=True, text_color='orange', background_color='white'),
        gui.RealtimeButton('▲', size=(1, 1), border_width=0,
                           button_color=(gui.theme_text_color(), gui.theme_background_color()), key='input_3_up'),
        gui.RealtimeButton('▼', size=(1, 1), border_width=0,
                           button_color=(gui.theme_text_color(), gui.theme_background_color()),
                           key='input_3_down')
    ]

    Spinner_4 = [
        gui.Input('0', size=(5, 1), justification='r', key='number_input_4', enable_events=True, text_color='orange', background_color='white'),
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
        [gui.Text(f"{_V_INIT_2_[-1]:02d}", size=(5, 1), key="display_number_1", background_color='white', text_color='green', font=('Helvetica', 12, 'bold'))],
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
        [gui.Text(f"{_V_INIT_2_[-1]:02d}", size=(5, 1), key="display_number_2", background_color='white', text_color='green', font=('Helvetica', 12, 'bold'))],
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
            _V_INIT_1_.append(_V_INIT_1_[-1] + 1)
            if _V_INIT_1_[-1] >= _V_INIT_2_[-1]:
                _V_INIT_2_ = _V_INIT_1_ + [_V_INIT_1_[-1] + 1]
                main_window.find_element("number_input_2").update(_V_INIT_2_[-1])
            main_window.find_element("number_input_1").update(_V_INIT_1_[-1])
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        elif events == "input_1_down":
            try:
                if len(_V_INIT_1_) > 2:
                    del _V_INIT_1_[-1]
            except IndexError:
                _V_INIT_1_ = [0, 1]
            if _V_INIT_1_[-1] >= _V_INIT_2_[-1]:
                _V_INIT_2_ = _V_INIT_1_ + [_V_INIT_1_[-1] + 1]
                main_window.find_element("number_input_2").update(_V_INIT_2_[-1])
            main_window.find_element("number_input_1").update(_V_INIT_1_[-1])
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        if events == "input_2_up":
            _V_INIT_2_.append(_V_INIT_2_[-1] + 1)
            main_window.find_element("number_input_2").update(_V_INIT_2_[-1])
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        elif events == "input_2_down":
            try:
                if len(_V_INIT_2_) > 2:
                    del _V_INIT_2_[-1]
            except IndexError:
                _V_INIT_2_ = [0, 1]
            if _V_INIT_1_[-1] == _V_INIT_2_[-1]:
                del _V_INIT_1_[-1]
                main_window.find_element("number_input_1").update(_V_INIT_1_[-1])
            main_window.find_element("number_input_2").update(_V_INIT_2_[-1])
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
            _V_INIT_3_.append(_V_INIT_3_[-1] + 1)
            if _V_INIT_3_[-1] >= _V_INIT_4_[-1]:
                _V_INIT_4_ = _V_INIT_3_ + [_V_INIT_3_[-1] + 1]
                main_window.find_element("number_input_4").update(_V_INIT_4_[-1])
            main_window.find_element("number_input_3").update(_V_INIT_3_[-1])
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        elif events == "input_3_down":
            try:
                if len(_V_INIT_3_) > 2:
                    del _V_INIT_3_[-1]
            except IndexError:
                _V_INIT_3_ = [0, 1]
            if _V_INIT_3_[-1] >= _V_INIT_4_[-1]:
                _V_INIT_4_ = _V_INIT_3_ + [_V_INIT_3_[-1] + 1]
                main_window.find_element("number_input_4").update(_V_INIT_4_[-1])
            main_window.find_element("number_input_3").update(_V_INIT_3_[-1])
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        if events == "input_4_up":
            _V_INIT_4_.append(_V_INIT_4_[-1] + 1)
            main_window.find_element("number_input_4").update(_V_INIT_4_[-1])
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        elif events == "input_4_down":
            try:
                if len(_V_INIT_4_) > 2:
                    del _V_INIT_4_[-1]
            except IndexError:
                _V_INIT_4_ = [0, 1]
            if _V_INIT_3_[-1] == _V_INIT_4_[-1]:
                del _V_INIT_3_[-1]
                main_window.find_element("number_input_3").update(_V_INIT_3_[-1])
            main_window.find_element("number_input_4").update(_V_INIT_4_[-1])
            main_window.Refresh()
            time.sleep(_V_SLEEP_TIMER_)
        if events == "save_as":
            quad_check(values['number_input_1'], values['number_input_2'], values['number_input_3'], values['number_input_4'])
            main_window.find_element('number_input_1').Update(int(values['number_input_1']))
            main_window.find_element('number_input_2').Update(int(values['number_input_1']))
            main_window.find_element('number_input_3').Update(int(values['number_input_3']))
            main_window.find_element('number_input_4').Update(int(values['number_input_3']))
            main_window.Refresh()
            values['number_input_2'] = values['number_input_1']
            values['number_input_4'] = values['number_input_3']
            save_file = values["save_as"]
            bin_array = generate_bins(values, _C_ALPHABET_)
            generate_csv(bin_array=bin_array, file_name=save_file)
        print(events, values)
    pass


if __name__ == '__main__':
    main()
