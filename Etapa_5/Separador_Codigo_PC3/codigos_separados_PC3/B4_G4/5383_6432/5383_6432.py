from numpy import *

ent = input("").upper()

cont = 0
som = 0

while len(ent) > cont:
	if ent[cont] == "A":
		som = som + 0.12
	elif ent[cont] == "E":
		som = som + 0.12
	elif ent[cont] == "I":
		som = som + 0.12
	elif ent[cont] == "O":
		som = som + 0.12
	elif ent[cont] == "U":
		som = som + 0.12
	else: 
		som = som + 0.18
	cont += 1
	
print(round(som,2))