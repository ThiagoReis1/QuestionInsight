r = input().upper()
i =  0
soma = 0
while r != "S":
	if r == "SIM":
		soma = soma + 1
	i = i + 1
	r = input().upper()
print(soma)