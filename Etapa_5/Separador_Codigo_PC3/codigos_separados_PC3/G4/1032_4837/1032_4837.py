from math import*

e = float(input("valor da encomenda: "))
i = float(input("imposto 10: "))
t = int(input("taxa: "))


v = (e + i) + t
print(round(v, 2))
