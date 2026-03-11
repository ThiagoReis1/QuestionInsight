from math import * 
# peso em gramas
peso = float(input("peso racao: "))
diario = float(input("quantidade diaria: "))

total = peso - (6 * diario)
print(round(total, 4))