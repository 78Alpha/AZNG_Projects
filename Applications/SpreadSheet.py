import PySimpleGUI as gui
import os
import sys


def write_(data):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters2 = letters[letters.index(data["letter_start"]):letters.index(data["letter_end"])]
    _V_MAIN_LIST_ = []
    for i in range(int(data['number_start']), (int(data['number_end']) + 1)):
        if len(str(i)) < 2:
            i = f"0{i}"
        for letter_iter in letters2:
            for iteration in range(int(data["Tletter_start"]), (int(data["Tletter_end"]) + 1)):
                if len(str(iteration)) < 2:
                    iteration = f"0{iteration}"
                _V_MAIN_LIST_.append(f"{data['initial_letter']}{i}-{letter_iter}-{iteration}")
    with open("gui_test.csv", 'w+') as data:
        for entry in _V_MAIN_LIST_:
            data.write(f"{entry}\n")
    os.system("start gui_test.csv")


def write_2(data, alpha_range):
    modded_range = alpha_range[alpha_range.index(data["letter_start"]):alpha_range.index(data["letter_end"])]
    _V_MAIN_LIST_ = []
    for i in range(int(data['number_start']), (int(data['number_end']) + 1)):
        i = f"{i:02d}"
        for letter_iter in modded_range:
            for iteration in range(int(data["Tletter_start"]), (int(data["Tletter_end"]) + 1)):
                if len(str(iteration)) < 2:
                    iteration = f"{iteration:02d}"
                _V_MAIN_LIST_.append(f"{data['initial_letter']}{i}-{letter_iter}-{iteration}")
    with open("gui_test.csv", 'w+') as data:
        for entry in _V_MAIN_LIST_:
            data.write(f"{entry}\n")
    os.system("start gui_test.csv")


def micro_update(data, alpha_range):
    modded_range = alpha_range[alpha_range.index(data["letter_start"]):alpha_range.index(data["letter_end"])]
    _V_MAIN_LIST_ = []
    for i in range(int(0), (int(5) + 1)):
        i = f"{i:02d}"
        for letter_iter in modded_range:
            for iteration in range(int(data["Tletter_start"]), (int(data["Tletter_end"]) + 1)):
                if len(str(iteration)) < 2:
                    iteration = f"{iteration:02d}"
                _V_MAIN_LIST_.append(f"{data['initial_letter']}{i}-{letter_iter}-{iteration}")
    return _V_MAIN_LIST_


def main():
    max_range = [i for i in range(10000)]
    alpha_range = [letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYS"]
    _layout_ = [
        [gui.Text("EXAMPLE: F01-A-01")],
        [gui.Text("Initial Letter"), gui.DropDown(alpha_range, default_value=alpha_range[0], size=(5, 5), tooltip="Letter to appear in center of string", key="initial_letter", enable_events=True)],
        [gui.Text("Number Start"), gui.Spin(max_range, size=(5, 5), tooltip="Number to start for bin Columns", key="number_start", enable_events=True), gui.Text("Number End"), gui.Spin(max_range, size=(5, 5), tooltip="Number to end for bin columns", key="number_end", enable_events=True)],
        [gui.Text("Letter Start"), gui.DropDown(alpha_range, default_value=alpha_range[0], size=(5, 5), key="letter_start", tooltip="Letter you want the range to start with", enable_events=True), gui.Text( "Letter End"), gui.DropDown(alpha_range, default_value=alpha_range[1], size=(5, 5), tooltip="Letter you want the range to end with", key="letter_end", enable_events=True)],
        [gui.Text("Trailing Number Start"), gui.Spin(max_range, size=(5, 5), key="Tletter_start", enable_events=True), gui.Text("Trailing Number End"),
         gui.Spin(max_range, size=(5, 5), key="Tletter_end", enable_events=True)],
        [gui.Multiline("", key="live_update")],
        [gui.Button("Start", enable_events=True), gui.Button("Reset", enable_events=True), gui.Text('', key='f')]
    ]

    window = gui.Window("Test", layout=_layout_)
    while True:
        try:
            events, values = window.Read()
            print(events, values)
            if int(values["number_start"]) > int(values["number_end"]):
                window.find_element("number_end").Update(values["number_start"] + 1)
                window.Refresh()
            if int(values["Tletter_start"]) > int(values["Tletter_end"]):
                window.find_element("Tletter_end").Update(values["Tletter_start"] + 1)
                window.Refresh()
            if events == gui.WINDOW_CLOSED:
                break
            if events == "Start":
                write_(values)
            if events == "Reset":
                window.close()
                main()
            window.find_element("live_update").Update("")
            window.find_element("live_update").Update(micro_update(values, alpha_range))
            window.refresh()
        except PermissionError:
            gui.popup_error("FILE IS ALREADY OPEN PLEAE CLOSE FILE BEFORE GENERATING A NEW ONE", title="FILE OPEN")
        except TypeError:
            sys.exit()




if __name__ == "__main__":
    main()
