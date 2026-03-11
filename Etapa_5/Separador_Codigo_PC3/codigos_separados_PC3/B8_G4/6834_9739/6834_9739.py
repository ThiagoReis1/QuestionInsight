from numpy import* 

n = input()

i = 0
b = 10.50
c = 8.75
d = 17.90
soma = 0 
while i < len(n):
	if n[i] == "C":
		soma = soma + b
	elif n[i] == "E":
		soma = soma + c
	elif n[i] == "P":
		soma = soma + d
	i = i + 1
print(round(soma, 2))