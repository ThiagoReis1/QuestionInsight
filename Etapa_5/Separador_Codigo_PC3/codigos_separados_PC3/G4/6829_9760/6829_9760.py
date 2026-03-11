a = input()
i = 0
soma = 0 

while i < len(a):
	if a[i] == "A":
		soma = soma + 19.90
	elif a[i] == "L":
		soma = soma + 3.50
	else:
		soma = soma + 4.25
	i = i + 1

print(round(soma, 2))