from numpy import *

s = input("insira a string: ").upper()

i = 0
soma = 0

while i < len(s):
	if s[i] == "D":
		soma = soma + 2.25
	elif s[i] == "S":
		soma = soma + 4.00
	else:
		soma = soma + 6.90
	i += 1
print(round(soma,2))