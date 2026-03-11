from math import *
p = float(input("Qual o valor de p: "))
f = 2**(1+p/1000)
s = p*pi**2/3141
d = 2*sqrt(p/40)
print(float(round(f, 2)))
print(float(round(s, 2)))
print(float(round(d, 2)))