from math import*
n=int (input("n "))
#snowberry
sn = float(((5**0.5)-1)/4)*n
#sais de fogo
sf=float((5-2*(5**0.5))**0.5)*n
#amanita
am=float (5*(5-2*(5**0.5)))*n
print(round(sn,2))
print(round(sf,2))
print(round(am,2))