import re

_C_BIN_FORMAT_REGEX_ = re.compile("^P-[0-9]-[A-Z]{1}[0-9]{3}[A-Z]{1}[0-9]{3}$")
_C_POD_ID_REGEX_ = re.compile("^HB05[0-9]{9}")
_C_BIN_LABEL_REGEX_ = re.compile("^[0-9]{1}[A-Z]{1}")
_C_SPLIT_BY_: list = [" \t", "\t"]
_C_FACE_REGEX_ = re.compile("^[A-Z]{1}")


def splitToBin(initial, splitter=_C_SPLIT_BY_):
    initialUpper = initial.upper()
    splitList = initialUpper.split(splitter[0]) if splitter[0] in initialUpper else initialUpper.split(splitter[1])
    return splitList


def getPodID(initial, podRegex=_C_POD_ID_REGEX_):
    tempID = podRegex.match(initial.upper())
    return tempID


def getBinLabels(initial, labelRegex=_C_BIN_LABEL_REGEX_):
    labelArray = [label for label in initial if labelRegex.match(label)]
    return labelArray


def stringOfElement(initial):
    return initial.group(0)


def getBinArray(initial, binRegex=_C_BIN_FORMAT_REGEX_):
    binList = [podBin for podBin in initial if binRegex.match(podBin)]
    binList.remove(binList[0])
    return binList


def userInputAsBin(initial, binRegex=_C_BIN_FORMAT_REGEX_):
    userBin = binRegex.match(initial.upper())
    return userBin


def getFaces(initial, faceRegex=_C_FACE_REGEX_):
    faceArray = [face for face in initial if faceRegex.match(face) and len(face) == 1]
    return faceArray
