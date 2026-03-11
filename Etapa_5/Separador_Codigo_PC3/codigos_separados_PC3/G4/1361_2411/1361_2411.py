from math import*
P = int(input("Quantidade de poções?"))

snow = (5**0.5-1)/4
sais = sqrt(5 - 2*(5**0.5))
amanita = 5*(5-2*sqrt(5))

A = snow * P
B = sais * P
C = amanita * P

print(round(A,2))
print(round(B,2))
print(round(C,2))
