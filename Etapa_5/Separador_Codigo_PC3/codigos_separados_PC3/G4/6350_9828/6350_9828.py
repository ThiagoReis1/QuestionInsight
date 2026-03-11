from numpy import *

m = input("N: ")
n = list(m)

if n[1] == "u" or n[1] == "U":
	c = 0
	a = ''
	while c < len(n):
		n[c] = n[c].upper()
		a = a + n[c]
		c += 1
	print(a)
else:
	print("nome invalido")