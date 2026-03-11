from math import *
p = float(input("Digite o valor do peso: "))
gd = 2**(1+p/1000)
gs = p*(pi**2)/3141
go = 2 * sqrt(p/40)
print (round(gd, 2))
print (round(gs, 2))
print (round(go, 2))