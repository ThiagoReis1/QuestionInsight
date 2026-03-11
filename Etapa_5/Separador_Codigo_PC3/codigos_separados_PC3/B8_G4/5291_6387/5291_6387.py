a = input("Gostou:  ").upper()
soma = 0
i = 0
while (a != "S"): 
	if a == "SIM":
	   soma = soma + 1
	   i = i +1
	elif a == "NAO":
		i = i + 1 
	a = input("Gostou: ").upper()
x = (soma * 100)/i
print(i)
print(round(x,2))