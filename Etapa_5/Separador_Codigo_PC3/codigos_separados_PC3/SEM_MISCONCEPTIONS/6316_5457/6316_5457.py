from numpy import *
p = input("produtos: ")

t = 0
s = 0
v = 0
i = 0
cont = 0

while i < len(p):
	if p[i] == "D":
		cont = cont + 2.25
		t = t + 1
	elif p[i] == "S":
		cont = cont + 4.00
		s = s + 2
	elif p[i] == "I":
		cont = cont + 6.90
		v = v + 3
	i = i + 1	
print(round(cont, 2)