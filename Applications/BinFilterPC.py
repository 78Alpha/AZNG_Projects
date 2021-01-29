import re
import time

_C_DATA_FORMAT_REGEX_ = re.compile("^[A-M]{1}[1-4]{1}[A-M]{1}[ ]P-[0-9]-[A-Z]{1}[0-9]{3}[A-Z]{1}[0-9]{3}[ ][A-Za-z]{8}$")
_C_POD_ID_REGEX_ = re.compile("^[0-9]{9}$")
_C_RECIPE_REGEX_ = re.compile("^[0-9]{3}-[0-9]{5}-[0-9]{3}")
prototype = re.compile("^pod (.*?)$")
_C_CRECIPE_VERSION_ = re.compile(" \t[0-9]{1}")
# 790-00265-021
# _C_POD_ID_REGEX_ = re.compile("^HB05[0-9]{9}")
# _C_BIN_LABEL_REGEX_ = re.compile("^[0-9]{1}[A-Z]{1}")
# _C_SPLIT_BY_: list = [" \t", "\t"]
# _C_FACE_REGEX_ = re.compile("^[A-Z]{1}")
#
# with open("example.txt", 'r') as data:
#     main_info = data.readlines()
#     data.close()


def getPodID(data):
    array = []
    data = data.split("\n")
    print(data)
        # print(new_data)
        # new_data = data
    tempID = ''
    for item in data:
        print(item[-9:])
        # podID = re.match(_C_POD_ID_REGEX_, item[-9:]).group(0)
        try:
            podID = int(item[-9:])
            # tempID = podID
        except:
            pass
    return f"HB05{podID}"


def getPodRecipe(data):
    array = []
    try:
        new_data = data.split("\n")
        # print(new_data)
    except:
        new_data = data
    recipe = ''
    count = 0
    version = ''
    for item in new_data:
        # print(item)
        # print(item) if "790" in item else print('')
        recipe = re.match(_C_RECIPE_REGEX_, item) if re.match(_C_RECIPE_REGEX_, item) is not None else recipe
        try:
            if count == 0:
                recipe.group(0)
                new_item = item.split('\t')
                version = new_item[1].strip(' ')
                count += 1
            else:
                pass
        except:
            pass
        # print(recipe)
        # version = re.match(_C_CRECIPE_VERSION_, item) if re.match(_C_CRECIPE_VERSION_, item) is not None else version
        # print(recipe, version)
    altered_header = f"00,{recipe.group(0)},0{version},00U,00,0000*00*00T10:00Z,00"
    # print(altered_header)
    return altered_header


def init_match(data):
    array = []
    try:
        new_data = data.split("\n")
    except:
        new_data = data
    for line in new_data:
        userBin = re.match(_C_DATA_FORMAT_REGEX_, line)
        try:
            array.append(userBin.group(0))
        except:
            pass
    return array


# def init_filtering(array):
#     new_array = []
#     for item in array:
#         temp_item = item.split(" ")
#         temp_item.pop(-1)
#         new_array.append(temp_item)
#     return new_array

def init_filtering(array):
    faces = []
    label = []
    bins = []
    for item in array:
        try:
            temp_item = item.split(" ")
        except:
            pass
        temp_item.pop(-1)
        faces.append(temp_item[0][0])
        label.append(f"{temp_item[0][1]}{temp_item[0][2]}")
        bins.append(f"{temp_item[1]}")
    return [faces, label, bins]


def face_filter(new_array):
    configuration = {"A": {}, "B": {}, "C": {}, "D": {}}
    for i in range(len(new_array)):
        try:
            configuration[f"{new_array[i][0][0]}"][f"{new_array[i][0][2]}"].append(f"{new_array[i][1]}")
        except KeyError:
            configuration[f"{new_array[i][0][0]}"][f"{new_array[i][0][2]}"] = [f"{new_array[i][1]}"]
        # configuration.setdefault(configuration[f"{new_array[i][0][0]}"][f"{new_array[i][0][2]}"], []).append(configuration[f"{new_array[i][1]}"])
        # configuration[f"{new_array[i][0][0]}"][f"{new_array[i][0][2]}"] = [] if new_array[i][1] not in configuration[f"{new_array[i][0][0]}"][f"{new_array[i][0][2]}"] else configuration[f"{new_array[i][0][0]}"][f"{new_array[i][0][2]}"].append(new_array[i][1])

    return configuration

# array = init_match(main_info)
# new_array = init_filtering(array)
# getPodRecipe(main_info)
