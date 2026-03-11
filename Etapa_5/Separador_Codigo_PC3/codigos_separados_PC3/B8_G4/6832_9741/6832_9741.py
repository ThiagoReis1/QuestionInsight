from numpy import*
a = input().upper()

i = 0 
soma = 0
while i < len(a):
	if a[i] == "H":
		soma = soma + 5.40
	elif a[i] == "C":
		soma = soma + 8.95
	elif a[i] == "L":
		soma = soma + 4.50
	i = i + 1
print(round(soma,2))