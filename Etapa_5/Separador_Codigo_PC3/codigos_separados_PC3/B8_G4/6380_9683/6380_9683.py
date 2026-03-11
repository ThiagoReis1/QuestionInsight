from numpy import *

a = zeros(4, dtype=int)

v = input("Insira o caractere:slaxd").upper().split(",")

for x in v:
	if x == "E":
		a[0] += 1
	elif x == "V":
		a[1] += 1
	elif x == "A":
		a[2] += 1 
	elif x == "D":
		a[3] += 1
print(a)