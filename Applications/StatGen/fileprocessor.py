import shutil
import os
import glob
import json
import pathlib
import time
import subprocess


def load_config(file_):
    file_path = pathlib.Path(file_)
    if not file_path.is_file():
        return False
    try:
        config_ = json.load(open(file_path))
        return config_
    except json.decoder.JSONDecodeError:
        return False

def save_config(values, time_bit):
    file_name = f"./config/config_{time_bit}.qbconfig"
    with open(file_name, "w") as f:
        try:
            json.dump(values, f)
            f.close()
            return True
        except json.decoder.JSONDecodeError:
            f.close()
            return False


def read_configs():
    configs_ = glob.glob("./config/*.qbconfig")
    return configs_


def startup_dir_creation():
    dir_s = [
        "./files",
        "./config",
        "./default"
    ]

    for dir_ in dir_s:
        if not os.path.exists(dir_):
            os.makedirs(dir_)

def prepare_udq(target_name):
    Downloads_Folder = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Downloads")
    file_ = glob.glob(f"{Downloads_Folder}\\udq*.csv")
    while len(file_) < 1:
        time.sleep(1)
        file_ = glob.glob(f"{Downloads_Folder}\\udq*.csv")
        if len(file_) < 1:
            pass
    shutil.move(file_[0], f"./files/{target_name}.csv")


def delete_old_files():
    old_files = glob.glob("./files/*.csv")
    if len(old_files) > 1:
        for file_ in old_files:
            os.remove(file_)
    Downloads_Folder = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Downloads")
    csv_files = glob.glob(f"{Downloads_Folder}\\udq*.csv")
    if len(csv_files) > 1:
        for udq in csv_files:
            os.remove(udq)


def open_stats():
    check_ = pathlib.Path("./files/stats.csv")
    if check_.is_file() and os.path.getsize(check_) > 0:
        subprocess.Popen(["start", "./files/stats.csv"])
        return True
    else:
        return False


def stat_file_gen(data_):
    by_user, by_floor = (35, 6)
    target_data = {}

    for key, value in data_.items():
        try:
            temp_data = open(f"./files/{key}.csv").readlines()
            target_data[key] = temp_data
        except:
            pass

    dbf_buf = by_floor - len(target_data["drive_by_floor"])

    fbf_buf = by_floor - len(target_data["floor_by_floor"])

    gbf_buf = by_floor - len(target_data["gaps_by_floor"])
    dbu_buf = by_user - len(target_data["drive_by_user"])
    fbu_buf = by_user - len(target_data["floor_by_user"])
    sbu_buf = by_user - len(target_data["station_by_user"])

    with open("./files/stats.csv", "w+") as csvfile:
        csvfile.write("GAP BY FLOOR\n")
        for line in target_data["gaps_by_floor"]:
            csvfile.write(line)
        for line in range(gbf_buf):
            csvfile.write("\n")
        # print("GAP BY FLOOR\n")
        csvfile.write("DRIVE BY FLOOR\n")
        for line in target_data["drive_by_floor"]:
            csvfile.write(line)
        for line in range(dbf_buf):
            csvfile.write("\n")
        # print("DRIVE BY FLOOR\n")
        csvfile.write("FLOOR BY FLOOR\n")
        for line in target_data["floor_by_floor"]:
            csvfile.write(line)
        for line in range(fbf_buf):
            csvfile.write("\n")
        # print("FLOOR BY FLOOR\n")
        csvfile.write("DRIVE BY USER\n")
        for line in target_data["drive_by_user"]:
            csvfile.write(line)
        for line in range(dbu_buf):
            csvfile.write("\n")
        # print("DRIVE BY USER\n")
        csvfile.write("FLOOR BY USER\n")
        for line in target_data["floor_by_user"]:
            csvfile.write(line)
        for line in range(fbu_buf):
            csvfile.write("\n")
        # print("STATION BY USER\n")
        csvfile.write("STATION BY USER\n")
        for line in target_data["station_by_user"]:
            csvfile.write(line)
        for line in range(sbu_buf):
            csvfile.write("\n")
        csvfile.write("END\n")
        csvfile.close()


def check_default():
    default = glob.glob("./default/*.qbconfig")
    if len(default) > 0:
        if os.path.exists(default[0]):
            return True, default[0]
        else:
            return False, None
    else:
        return False, None
