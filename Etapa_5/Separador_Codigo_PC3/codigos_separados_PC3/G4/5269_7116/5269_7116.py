np = int(input(": "))
cont = 0
i = 0

while (np != 0):
	if(np > 0):
		i = i + 1
		if (np % 3 == 0):
			cont = cont + 1
		np = int(input(": "))

por = cont * 100 / i 
print(i)
print(round(por, 2))