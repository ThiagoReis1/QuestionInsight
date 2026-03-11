from math import*
qdp = float(input("quantidade de pocoes: "))

s = (sqrt(5)-1)/4 * qdp
sf = sqrt(5-2*sqrt(5)) * qdp
a = 5*(5-2*sqrt(5)) * qdp

print(round(s,2))
print(round(sf,2))
print(round(a,2))