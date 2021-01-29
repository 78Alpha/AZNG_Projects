import re

_C_DATA_FORMAT_REGEX_ = re.compile("^[A-M]{1}[1-4]{1}[A-M]{1}[ ]P-[0-9]-[A-Z]{1}[0-9]{3}[A-Z]{1}[0-9]{3}[ ][A-Za-z]{8}$")
_C_POD_ID_REGEX_ = re.compile("^[0-9]{9}$")
_C_RECIPE_REGEX_ = re.compile("^[0-9]{3}-[0-9]{5}-[0-9]{3}")
_C_CRECIPE_VERSION_ = re.compile(" \t[0-9]{1}")


def getPodID(data: list) -> str:
    tempID: str = ''
    for item in data:
        try:
            podID: int = int(item[-9:])
            break
        except:
            pass
    return f"HB05{podID}"


def getPodRecipe(data: list) -> str:
    recipe: str = ''
    count: int = 0
    version: str = ''
    for item in data:
        recipe = re.match(_C_RECIPE_REGEX_, item) if re.match(_C_RECIPE_REGEX_, item) is not None else recipe
        try:
            if count == 0:
                recipe.group(0)
                new_item = item.split('\t')
                version = new_item[1].strip(' ')
                count += 1
            else:
                break
        except:
            pass
    altered_header: str = f"00,{recipe.group(0)},0{version},00U,00,0000*00*00T10:00Z,00"
    return altered_header


def init_match(data: list) -> list:
    array: list = []
    for line in data:
        userBin = re.match(_C_DATA_FORMAT_REGEX_, line)
        try:
            array.append(userBin.group(0))
        except:
            pass
    return array


def init_filtering(array: list) -> list:
    factored_array = {"faces": [], "label": [], "bins": []}
    for item in array:
        try:
            temp_item: list = item.split(" ")
        except:
            pass
        temp_item.pop(-1)
        factored_array['faces'].append(temp_item[0][0])
        factored_array['label'].append(f"{temp_item[0][1]}{temp_item[0][2]}")
        factored_array['bins'].append(f"{temp_item[1]}")
    return factored_array


def face_filter(new_array: list) -> dict:
    configuration: dict = {"A": {}, "B": {}, "C": {}, "D": {}}
    for i in range(len(new_array)):
        try:
            configuration[f"{new_array[i][0][0]}"][f"{new_array[i][0][2]}"].append(f"{new_array[i][1]}")
        except KeyError:
            configuration[f"{new_array[i][0][0]}"][f"{new_array[i][0][2]}"] = [f"{new_array[i][1]}"]
    return configuration

