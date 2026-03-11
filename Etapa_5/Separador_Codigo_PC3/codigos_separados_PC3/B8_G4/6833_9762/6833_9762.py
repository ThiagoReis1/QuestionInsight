from numpy import*
a = input().upper()
i = 0
m = 7.25
p = 4.75
r = 3.50
soma =  0 
while i < len(a):
	if a[i] == "M":
		soma = soma + m
	elif a[i] == "P":
		soma = soma + p
	elif a[i] == "R":
		soma = soma + r
	i = i + 1
print(round(soma,2))