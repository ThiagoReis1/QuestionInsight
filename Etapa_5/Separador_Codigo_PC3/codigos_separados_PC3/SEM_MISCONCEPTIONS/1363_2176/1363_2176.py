from math import *

p = float(input("Digite o peso (gramas):"))

Gflawless = 2**(1+(p/1000)) 
GSoul = p * ((pi**2)/3141)
GOleo = 2 * sqrt(p/40)

print(round(Gflawless,2))
print(round(GSoul,2))
print(round(GOleo,2))