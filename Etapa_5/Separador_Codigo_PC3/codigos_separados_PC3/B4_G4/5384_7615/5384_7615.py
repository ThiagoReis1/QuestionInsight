from numpy import *
v= input("digite a palavra: ").upper()
a= 0
i= 0

while i < len(v):
	if v[i] == "A":
		a= a + 45.15
	elif v[i] == "E":
		a= a + 45.15
	elif v[i] == "I":
		a= a + 45.15
	elif v[i] == "O":
		a= a + 45.15
	elif v[i] == "U":
		a= a + 45.15
	else:
		a= a + 50.17
	i+=1

print(round(a,2))