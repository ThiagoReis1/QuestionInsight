from math import *

peso = (float(input("peso do saco de racao em gramas: ")))
quantidade = (float(input("quantidade diaria de racao em gramas: ")))

total = peso - (quantidade * 5)

print(round(total, 3))

