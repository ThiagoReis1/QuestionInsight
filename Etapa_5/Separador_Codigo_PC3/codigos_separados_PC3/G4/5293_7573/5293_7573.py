nt = int(input("Digite o numero: "))

pares = 0
cont = 0

while (nt != 0):
	if (nt%2 == 0):
		pares = pares+1
	nt = int(input("Digite o numero: "))
	cont = cont + 1
cal1 = (pares*100)/cont
print(cont)
print(round(cal1,2))

	