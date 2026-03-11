from numpy import *

l = input("Lista de compras: ").upper()
i = 0
t = len(l) - 1
h = 0
ll = 0
e = 0
while i <= t:
	if l[i] == 'H':
		h += 1
	elif l[i] == 'L':
		ll += 1
	else:
		e += 1
	i += 1	
t = h*3.85 + ll*2.95 + e*7.90
print(round(t,2))