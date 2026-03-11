from math import*

peso = float(input("peso da bagagem: "))

frete = (peso * 43.21) + 25
total = (frete * 62/100) + frete

print(round(total,2))