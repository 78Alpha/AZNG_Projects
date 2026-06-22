import FreeSimpleGUI as gui

import core
import fileprocessor
import timekeeper
import sys

version_ = "1.0.0"

custom_button = b"iVBORw0KGgoAAAANSUhEUgAAAGQAAAAjCAYAAABiv6+AAAAACXBIWXMAAAOkAAADpAGRLZh1AAAC0UlEQVRoge2br24iURSHfyXBgJkaDIhBY4rB0kdAXtk+QeENtk/Q7hO0dVfyCJCgMGAwGEaAwTAGDGbzm5zLDgVaIMB0l/MlhKYJDHO+nHvunzM3OABrrQegBqAKwAdwB8A75DuugBBAH0AAoA2gaYwJ973tvYRYa+8BPIkM5HK56JXJZJDNZq9dwBrz+RyLxQLT6TR6CU0Av40xre8+/6UQay2z4IUiKMD3fRSLxdPfxX/MaDRCEARODsU0jDHBrjveKcRa+0AZ2WzWq1QqUUYox0Mh3W6XGRSKlPe9hVhr65TBbCiXy0in06riBCyXS/R6vShrRMrr52/dEOJkMCt0eDoPFMJs2SZlTYgMU28q4/zEpDzGh6+U+8MVcIpQGecnFucXiX1EKnblqICzZiiXgbFmzGUm+1eIrDNqHKq0gF8OxpoxZ+zFwSpDntxiT7kssbhz4Y0b2Q6ZaSFPjliBv0257RCVkRyFQsFdu0YhVR2qkoW1RBxUKcRXIckjDnwKueOurZIs4uCOQjzdQk8eceClfvjvvDoiIdyFVJLFOaCQVhjufcKonAlx0KKQcDabaZwTRhyEFNKOnf0qCSEO2hTS5Pg1mUzURUIw9lJDmik5cG+pkOSQI90WXbhp7wf/qcX98jDmkgwfcNNeOULs8wBeuSwS8747xo0vDBssLMPhUJVcCMZainnDXXElRLrqnmlMZ13nhzGW7HiOdzSubZ0YY34BeO90OlpPzghjyxgz1hLzFbsa5d4APOgp4umJnQ5SxuPnC3zVSspOiHo+n3fdEf/Ujf802ITNIUpmVK/GmMa2n/hdszU7IZgtPjOlVCqpmAOhiMFg4NYagTTG7eyC3/dxhLp0Rfie50VnwHyPHT0qAos1V92sE+Px2NXiQB5H2OjlPUpITIx7WOdeHtZRdsOHdpgJbWNMc984HSRkiyBPxWzARd5xU1QAfwDvPzbqRGQg7QAAAABJRU5ErkJggg=="


def popup_(message, error=False, caution=False):
    error_data = b"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"

    success_data = b"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"

    caution_data = b"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"

    if not caution:
        image_data = success_data
        window_name = "Success"
        if error:
            image_data = error_data
            window_name = "Error"
    else:
        window_name = "Warning"
        image_data = caution_data

    layout = [
        [gui.Image(data=image_data, size=(64, 64))],
        [gui.Text(message)]
    ]

    window = gui.Window(window_name, layout=layout, keep_on_top=True)
    window.Read()


def main():

    time_list = timekeeper.time_table_generator()
    time_zones = timekeeper.time_zones
    fileprocessor.startup_dir_creation()
    config_ = core.check_default()
    configs_ = core.read_configs()

    if config_ is not None:
        layout = [
            [gui.Text("Start",
                      text_color='orange',
                      background_color='white'),
             gui.Spin([item for item in time_list],
                      key="SOS",
                      initial_value=config_["SOS"],
                      text_color='grey',
                      background_color='white'),
             gui.Text("End",
                      text_color='orange',
                      background_color='white'),
             gui.Spin([item for item in time_list],
                      key="EOS",
                      initial_value=config_["EOS"],
                      text_color='grey',
                      background_color='white'),
             gui.DropDown(time_zones,
                          default_value=config_["Timezone"],
                          key="Timezone",
                          text_color='grey',
                          background_color='white',
                          button_background_color='white',
                          button_arrow_color='orange')],
            [gui.DropDown(configs_,
                          key="Configs",
                          text_color='grey',
                          background_color='white',
                          button_background_color='white',
                          button_arrow_color='orange'),
             gui.Button("Reload",
                        image_data=custom_button,
                        button_color=('orange', 'white'),
                        border_width=0)],
            [gui.Text("Password",
                      text_color='orange',
                      background_color='white'),
             gui.InputText(config_["Password"],
                           key="Password",
                           size=(10, 8),
                           text_color='grey',
                           background_color='white'),
             gui.Text("Site",
                      text_color='orange',
                      background_color='white'),
             gui.InputText(config_["Site"],
                           key="Site",
                           size=(10, 8),
                           text_color='grey',
                           background_color='white')],
            [gui.Button("Run",
                        key="Run",
                        image_data=custom_button,
                        button_color=('orange', 'white'),
                        border_width=0),
             gui.Button("Save",
                        key="Save",
                        image_data=custom_button,
                        button_color=('orange', 'white'),
                        border_width=0),
             gui.Button("Load",
                        key="Load",
                        image_data=custom_button,
                        button_color=('orange', 'white'),
                        border_width=0)],
        ]
    else:
        layout = [
            [gui.Text("Start",
                      text_color='orange',
                      background_color='white'),
             gui.Spin([item for item in time_list],
                      key="SOS",
                      text_color='grey',
                      background_color='white'),
             gui.Text("End",
                      text_color='orange',
                      background_color='white'),
             gui.Spin([item for item in time_list],
                      key="EOS",
                      text_color='grey',
                      background_color='white'),
             gui.DropDown(time_zones,
                          default_value="America/Los_Angeles",
                          key="Timezone",
                          text_color='grey',
                          background_color='white',
                          button_background_color='white',
                          button_arrow_color='orange')],
            [gui.DropDown(configs_,
                          key="Configs",
                          text_color='grey',
                          background_color='white',
                          button_background_color='white',
                          button_arrow_color='orange'),
             gui.Button("Reload",
                        image_data=custom_button,
                        button_color=('orange', 'white'),
                        border_width=0)],
            [gui.Text("Password",
                      text_color='orange',
                      background_color='white'),
             gui.InputText("",
                           key="Password",
                           size=(10, 8),
                           text_color='grey',
                           background_color='white'),
             gui.Text("Site",
                      text_color='orange',
                      background_color='white'),
             gui.InputText("",
                           key="Site",
                           size=(10, 8),
                           text_color='grey',
                           background_color='white')],
            [gui.Button("Run",
                        key="Run",
                        image_data=custom_button,
                        button_color=('orange', 'white'),
                        border_width=0),
             gui.Button("Save",
                        key="Save",
                        image_data=custom_button,
                        button_color=('orange', 'white'),
                        border_width=0),
             gui.Button("Load",
                        key="Load",
                        image_data=custom_button,
                        button_color=('orange', 'white'),
                        border_width=0)],
        ]

    window = gui.Window(title=f"Stat File Generator {version_}", layout=layout, background_color='white')

    while True:
        events, values = window.Read()  # values are json and can be saved/loaded easily
        # print(events, values)
        if events == gui.WIN_CLOSED or events is None:  # Force kill Window
            window.close()
            sys.exit()
        if events == "Run":
            result_ = core.compare_password(values["Password"])
            if result_ is False:
                popup_("Password Is Incorrect!", error=True)
                continue
            else:
                pass
            if values["Site"] == "":
                popup_("Site Can't Be Empty!", error=True)
                continue
            else:
                values["Site"] = values["Site"].upper()

            popup_("Close all open Stat files to generate a new one! Close this window when finished.", caution=True)
            result = core.run_stats(values)
            if result != "Success":
                popup_(result, error=True)
            elif result == "Success":
                popup_(result, error=False)
            else:
                pass
            #timekeeper.convert_time(values["SOS"], values["EOS"], values["Timezone"])
            pass
        elif events == "Save":
            result = core.save_config(values)
            if result != "Success":
                popup_(result, error=True)
            else:
                popup_("Config saved to Configs folder!", error=False)
                configs_ = core.read_configs()
                window.find_element("Configs").update(values=configs_)
                window.Refresh()
        elif events == "Load":
            updateable = ["SOS", "EOS", "Timezone", "Site", "Password"]
            result = core.load_config(values["Configs"])
            if type(result) is dict:
                for update in updateable:
                    window.find_element(update).update(result[update])
                window.Refresh()
            else:
                popup_(result, error=True)
            pass
        elif events == "Reload":
            configs_ = core.read_configs()
            window.find_element("Configs").update(values=configs_)
            window.Refresh()

if __name__ == "__main__":
    main()
