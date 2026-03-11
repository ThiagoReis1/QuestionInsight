v = float(input("digite: "))
c = float(input("digite: "))
j = float(input("digite: "))
taxa = j / 100
cont = 0
a = v
while (cont < v):
	if (v < 0) and (c < 0) and (j < 0):
		print("Dados incorretos")
		saldo = c - taxa
		a = a + (saldo * taxa)
		cont = cont + 1
	print(round(cont, 2))
	
	
