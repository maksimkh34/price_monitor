from Color import Color
import requests


def start_text():
    print(Color.blue + "\t\t\t\tItem Price Monitor\n\t\t\t\t\t\tv1.0\n")
    print(Color.blue + "Connecting buff...\t", end="")
    if requests.get("https://buff.163.com/").status_code == 200:
        print("Done! ")
    else:
        print(Color.red + "Error. Exiting")
        exit(-1)


def menu():
    print(Color.yellow + "[" + Color.green + "0" + Color.yellow + "]" + Color.blue + " Monitor all listed items")
    print(Color.yellow + "[" + Color.green + "1" + Color.yellow + "]" + Color.blue + " Monitor certain "
                                                                                     "item from list by number")
    print(Color.yellow + "[" + Color.green + "2" + Color.yellow + "]" + Color.blue + " Print list of tracked items")
    print(Color.yellow + "[" + Color.green + "3" + Color.yellow + "]" + Color.blue + " Edit tracked items list")
    print(Color.yellow + "[" + Color.green + "4" + Color.yellow + "]" + Color.blue + " Exit")
    print(Color.yellow + "Your choice: ", end="")
    return int(input())


def exit_banner():
    print(Color.green + 'Exiting!')
