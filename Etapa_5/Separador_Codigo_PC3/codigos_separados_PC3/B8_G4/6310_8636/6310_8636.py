from numpy import*

p = input("produtos: ").upper()

i = 0
cont = 0

while i < len(p):
	if p[i] == "M":
		cont = cont + 7.25
	elif p[i] == "P":
		cont = cont + 4.75
	elif p[i] == "R":
		cont = cont + 3.50
	i = i + 1
	
print(round(cont, 2)), len("M"), len("P"), len("R")