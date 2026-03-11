n = int(input("numero de 6 digitos "))
pp = n//1000 #primeira parte
sp = n % 1000 #segunda parte 
print(pp)
print(sp)
from math import*
v = (pp-sp)**2
if (n == v):
	m = "atende"
else:
	m = "nao atende"
print(m)
print(n)