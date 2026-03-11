from math import* 
L = float(input("quantidade de litros: "))
y = (2.86*L) + 50
p = y*(34/100)
total = (y+p)
print(round(total,2))