numero = int(input("digite o valor do numero para raiz:"))
cont = 1

while (cont <= numero):
	raiz = (cont)**(0.5)
	cont = cont + 1
	print(round(raiz, 2))
print("fim")