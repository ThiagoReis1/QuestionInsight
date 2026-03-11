from numpy import*

cor = input("Cor do cabelo:").split(',')

cont = 0

for i in cor:
	if (cor == "P"):
		cont = cont + 1
	if (cor == "C"):
		cont = cont + 1 
	if (cor == "R"):
		cont = cont + 1
	if (cor == "L"):
		cont = cont + 1
	if (cor == "B"):
		cont = cont + 1
	print(cont)