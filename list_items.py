from Color import Color
from Item import Item
from progressbar import progressbar


def import_db():
    rdb = open("list")
    items = []
    lines = []
    for line in rdb:
        lines.append(line)

    for line in progressbar(lines):
        item = Item(line.split(':')[0], line.split(':')[1], line.split(":")[2].replace("\n", ""))
        items.append(item)
    return items


def print_items(items):
    total_profit = 0
    for item in items:
        total_profit += float(item.print())
    print(Color.blue + "\n\t\tTotal profit: ", end="")
    if total_profit > 0:
        print(Color.green, end="")
    else:
        print(Color.red, end="")
    print("{:.2f}".format(total_profit))
