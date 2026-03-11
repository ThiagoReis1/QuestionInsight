a = input("").upper()
i = 0
soma = 0
while i < len(a):
	if a[i] == "I":
		soma = soma + 3.75
	elif a[i] == "M":
		soma = soma + 4.5
	elif a[i] == "S":
		soma = soma + 2.9
	i = i + 1
print(round( soma , 2))