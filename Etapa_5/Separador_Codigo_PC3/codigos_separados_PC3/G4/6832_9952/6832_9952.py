from numpy import*
n = input("string")
i = 0
soma  = 0
while i < len(n):
	if n[i]=="H":
		soma = soma + 5.40
	elif n[i]=="C":
		soma = soma + 8.95
	else:
		soma = soma + 4.50
	i = i + 1
print(round(soma,2))