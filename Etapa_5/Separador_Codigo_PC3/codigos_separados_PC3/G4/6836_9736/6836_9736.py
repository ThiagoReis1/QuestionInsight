from numpy import *

a = input()
i = 0
soma = 0

while i < len(a):
	if a[i] == "B":
		soma = soma + 6.80
	elif a[i] == "C":
		soma = soma + 11.75
	else:
		soma = soma + 5.90
	i = i + 1
	
print(round(soma, 2))