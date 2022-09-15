import time
import urllib.request

def get_price():
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return float(text[start_of_price : end_of_price])

preco = input("Do you want to see the price now (Responda com Y para YES e N para NO)? ")
if preco == "S":
    print(get_price())
else:
    preco = 99.99
    while preco > 6.58:
        time.sleep(900)
        preco = get_price()
    print("compre")
