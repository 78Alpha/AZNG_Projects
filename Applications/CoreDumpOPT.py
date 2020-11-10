import json

# _C_DATA_HEADER_: str = "00,000*00000*000,00,00U,00,0000*00*00T10:00Z,00"
_C_DATA_HEADER_: str = "00,CUS*TOMRE*CIP,E.,00U,00,0000*00*00T10:00Z,00"


def generateBinConf(podID: str, binFaces: list, binLablels: list, binList: list):
    configuration: dict = {"POD-ID": podID, "FACES": {"A": {},
                                                      "B": {},
                                                      "C": {},
                                                      "D": {}}}
    for iterator in range(len(binLablels)):
        configuration["FACES"][f"{binFaces[iterator]}"][f"{binLablels[iterator][1]}"] = [] if binList[iterator] not in configuration["FACES"][f"{binFaces[iterator]}"][f"{binLablels[iterator][1]}"] else configuration["FACES"][f"{binFaces[iterator]}"][f"{binLablels[iterator][1]}"].append(binList[iterator])
    with open(f"{podID}.json", 'w+') as podConf:
        json.dump(configuration, podConf, indent=3)
        podConf.close()


def createRecipe(podID: str, binFaces: list, binLablels: list, binList: list, header: str = _C_DATA_HEADER_) -> None:
    recipe: str = f"{header}"
    recipe += ''.join([f">{binFaces[count]}{binLablels[count]}{binList[count].replace('-', '*')}" for count in range(len(binLablels))])
    recipe += "!"
    with open(f"{podID}.txt", 'w+') as podRecipe:
        podRecipe.write(recipe)
        podRecipe.close()
