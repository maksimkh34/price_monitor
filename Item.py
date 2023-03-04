import requests
from filters import filter_price
from Color import Color


class Item:
    def __init__(self, item_id, buy_price, numb):
        self.url = "https://buff.163.com/goods/" + item_id
        self.buy_price = buy_price
        response = requests.get(self.url)
        num = response.text.find("data-goods-market-hash-name=")+28
        self.name = response.text[num:num+50].split('\n')[0]
        self.price = filter_price(self.url)
        self.number = numb

    def print(self):
        profit = float(self.price) / float(self.buy_price)
        profit = "{:.2f}".format(profit)
        print(Color.yellow + "Item name: " + Color.blue + self.name.replace('"', ""))
        print(Color.yellow + "Buy price: " + Color.blue + self.buy_price + "¥")
        print(Color.yellow + "Now price is: " + Color.blue + self.price + "¥")
        print(Color.yellow + "Amount: " + Color.blue + str(self.number))
        print(Color.yellow + "Link: " + self.url)
        print(Color.yellow + "Profit: ", end="")
        if float(profit) < 1:
            print(Color.red, end="")
        if float(profit) == 1:
            print(Color.yellow, end="")
        if float(profit) > 1:
            print(Color.green, end="")

        print(profit + "x (", end="")
        if float(profit) < 1:
            print("-", end="")
        print(str(int(float(profit) * 100)) + "%)")
        print(Color.yellow + "Total profit: ", end="")
        if float(profit) < 1:
            print(Color.red, end="")
        if float(profit) == 1:
            print(Color.yellow, end="")
        if float(profit) > 1:
            print(Color.green, end="")
        print("{:.2f}".format(float(float(self.price) - float(self.buy_price))*float(self.number)) + "¥")
        print()
        return (float(float(self.price) - float(self.buy_price)))*float(self.number)
