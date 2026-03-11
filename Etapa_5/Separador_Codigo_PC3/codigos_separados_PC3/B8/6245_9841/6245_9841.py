n = str(input("resposta: ")).upper()
cont1 = 0
cont2 = 0
cont3 = 0
while n != "X":
	if n == "S":
		cont1 = cont1 + 1
	elif n == "I":
		cont2 = cont2 + 1
	elif n == "N":
		cont3 = cont3 + 1
	n = str(input("reposta: ")).upper()
print(cont1)