def filterConsoleToBins():
    with open("rows.txt", 'r') as console_file:
        rows = console_file.readlines()
        console_file.close()

    pod_id = input("SCAN POD BASE: ")
    with open(f"console_output_{pod_id}.txt", 'w+') as output_file:
        for row in rows:
            split_row = row.split(' ')
            output_file.write(split_row[1] + "\n")
            print(f"{split_row[0]}: {split_row[1]}")


# filterConsoleToBins()

def recipe_gen():
    pod_id = input("SCAN POD ID: ")
    recipe_ = input("RECIPE FROM POD CONSOLE: ")[:13]
    rceipe_version = input("RECIPE VERSION: ")[0]
    with open("rows.txt", 'r') as console_file:
        rows = console_file.readlines()
        console_file.close()
    recipe = "[Generated with QuickFilter V.01]\n\n"
    recipe += f"00,{recipe_.replace('-', '*')},0{rceipe_version},00U,00,0000*00*00T10:00Z,00"
    for row in rows:
        recipe += ">"
        temp = row.split(" ")
        recipe += f"{temp[0]}{temp[1].replace('-', '*')}"
    recipe += '!'
    with open(f"{pod_id}_recipe_card.txt", 'w+') as recipe_card:
        recipe_card.write(recipe)
        recipe_card.close()
    # pod_array = {
    #     "A": {},
    #     "B": {},
    #     "C": {},
    #     "D": {}
    # }
    # for row in rows:
    #     pod_array[f"{row[0]}"][f"{row[2]}"] = [] if row[2] not in pod_array[f"{row[0]}"] else \
    #         pod_array[f"{row[0]}"][f"{row[2]}"]

filterConsoleToBins()
