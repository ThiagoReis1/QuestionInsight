from math import*

peso = float(input("peso do saco: "))
quant = float(input("quantidade diaria: "))

result = peso - (quant * 7) 

print(round(result, 3))