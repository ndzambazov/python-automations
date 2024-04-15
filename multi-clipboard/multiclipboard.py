import sys
import clipboard
import json
import os

DATA_FILE = "clipboard.json"
DATA_PATH = os.path.dirname(__file__)
SAVED_DATA = "{}/{}".format(DATA_PATH, DATA_FILE)


def del_item(filepath, data):
    pass


def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_json(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except Exception:
        print("File doesnt exist .. Creating empty one.")
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_json(SAVED_DATA)

    if command == "save":
        print("OPERATION:", command)
        key = input("Enter name: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
    elif command == "load":
        print("OPERATION:", command)
        key = input("Enter name: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard!")
        else:
            print("Key doesnt exist!")
    elif command == "list":
        print("OPERATION:", command)
        print(json.dumps(data, indent=4))
    elif command == "delete":
        # TBD
        print("OPERATION:", command)
        key = input("Enter name: ")
        if key in data:
            del data[key]
            print(json.dumps(data, indent=4))
            save_items(SAVED_DATA, data)
    else:
        print("Unknown command")

else:
    print("1 argument allowed")

