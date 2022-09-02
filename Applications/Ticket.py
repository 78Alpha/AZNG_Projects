import random
import re

char_set = "abcdefghijklmnopqrstuvwxyz1234567890"
pod_id1 = re.compile(r"\w{2}\d{11}")
pod_id2 = re.compile(r"\d{9}")
pod_id3 = re.compile(r"\d{3}\s\d{3}\s\d{3}")
pod_id4 = re.compile(r"\d{3}-\d{3}-\d{3}")
pod_part = re.compile(r"\d{3}")
bin_id = re.compile(r"P-\d-[A-Z]\d{3}[A-Z]\d{3}")
zone_id = re.compile(r"A0\d")


def gen_128name():
    name = ''
    for i in range(128):
        name += random.choice(char_set)
    return name


def pull_info(string):
    pod = ''
    bin = ''
    zone = ''
    notes = ''
    parts = string.upper().split(" ")
    for part in parts:
        if pod_id1.match(part):
            pod = part
        elif pod_id2.match(part):
            pod = part
        elif pod_id3.match(part):
            pod = part
        elif pod_id4.match(part):
            pod = part
        elif pod_part.match(part):
            if len(pod) == 9:
                pass
            else:
                pod += part
        elif bin_id.match(part):
            bin = part
        elif zone_id.match(part):
            zone = part
        else:
            if part != "POD" and part != "BIN":
                notes += f"{part} "
    return zone, pod, bin, notes


def process_notes(notes):
    spill_keys = ["SPILL, SOAP, DETERGENT, LIQUID"]
    frame_keys = ["CLIP", "BAR", "CROSSBAR", "BEAM"]
    skirt_keys = ["RIP", "CUT", "HOLE", "TEAR"]
    category = ''
    note_check = notes.split(" ")
    for part in note_check:
        if part in spill_keys:
            category = "SPILL"
            break
        if part in frame_keys:
            category = "FRAME"
            break
        if part in skirt_keys:
            category = "SKIRT"
            break
    if category == '':
        category = input("Category not determined [SPILL, FRAME, SKIRT, RESKIRT, OTHER]: ").upper()
    return category


def safety_check():
    safety_class = input("Satey grade for ticket [SAFE (default), CAUTION, HAZARD, DANGER]: ").upper()
    if safety_class not in ["SAFE", "CAUTION", "HAZARD", "DANGER"]:
        safety_class = "SAFE"
    return safety_class


def tag_write(zone, pod, bin, category, safety):
    tag = f"{zone} {pod} {bin} [{category}] [{safety}]"
    return tag


def ticket_write(string):
    ticket_name = gen_128name()
    with open(f"{ticket_name}.txt", 'w+') as ticket:
        zone, pod, bin, notes
