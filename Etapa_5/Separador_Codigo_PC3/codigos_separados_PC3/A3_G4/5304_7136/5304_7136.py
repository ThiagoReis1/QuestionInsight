bi = int(input("numero inicial de bacterias: "))
h = int(input("horas totais: "))

cont = 0 
taxa = 15/100
total = bi

while cont < h:
	cres = int(taxa * bi)
	bi = bi + cres
	cont = cont + 1
	print(bi)
	