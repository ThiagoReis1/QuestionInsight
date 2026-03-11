from numpy import *

prog = input("Texto: ").upper()

vog = "aeiou"
carac = "bcdfghjklmnpqrstvwxyz"
i = 0
custo = 0
while len(prog) > i:
	if prog[i] == 'A' or prog[i] == "E" or prog[i] == "I" or prog[i] == "O" or prog[i] == "U":
		custo = custo + 45.12
	else:
		custo =custo + 50.18
	i = i + 1	
print(custo)		