x = input("SIM/NAO/S ").upper()
cont = 0

while x != 'S':
	if x == 'SIM':
		cont = cont + 1
	x = input("SIM/NAO/S ").upper()
print(cont)