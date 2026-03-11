from numpy import *

s = input("senha criada: ").upper()

i = 0
custo1 = 0
custo2 = 0

while i < len(s):
	if s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U":
		custo1 += 1.12
	else:
		custo2 += 1.18
	i += 1
	
soma = custo1 + custo2
print(round(soma, 2))