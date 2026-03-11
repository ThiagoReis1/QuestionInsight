from numpy import*

a = input()
i = 0
soma = 0
b = 10.50
c = 8.75
d = 17.90

while i < len(a):
	if a[i] == "C":
		soma = soma + b
	elif a[i] == "E":
		soma = soma + c
	elif a[i] == "P":
		soma = soma + d
	i = i + 1 
print(round(soma,2))