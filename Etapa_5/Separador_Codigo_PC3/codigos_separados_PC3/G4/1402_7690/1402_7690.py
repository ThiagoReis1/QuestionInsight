arma = input("machado ou lanca? ")
ft = int(input("valor entre 1 e 10: "))
if (arma == "machado"):
	dano = int((30*ft)/10)
	print (dano)
else:
	dano = int(5+((20*ft)/10))
	print (dano)