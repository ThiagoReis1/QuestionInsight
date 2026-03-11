from numpy import *

votos = input("insira:").upper().split(",")
c = zeros(4 , dtype=int)

for i in votos:
	if i == "A":
		c[0] += 1
	elif i == "B":
		c[1] += 1
	elif i== "C":
		c[2] += 1
	elif i== "D":
		c[3] += 1
		
print(c)
		