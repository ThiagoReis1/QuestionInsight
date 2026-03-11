from numpy import *

s = input("digite a senha: ").upper()

i=0
custo = 0
while i < len(s):
	if s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U":
		custo = custo + 1.12
	else:
		custo = custo + 1.18
	i = i+1
print(round(custo, 2))