import requests


def filter_price(url):
    buffResponse = requests.get(url)
    num = buffResponse.text.find(' data-type="small" data-original-currency="CNY"')
    price = buffResponse.text[num - 6:num]
    return price.replace('"', "").replace('=', "").replace("'", "")
