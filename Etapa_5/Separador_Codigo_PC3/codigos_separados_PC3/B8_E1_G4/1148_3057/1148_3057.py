r = (input ("Informe o nome da regiao: "))

if	(r=="Norte")or(r=="Vale")or(r=="Terras Fluviais")or(r=="Terras da Tempestade")or(r=="Dorne")or(r=="Ilhas de Ferro")or(r=="Campina")or(r=="Terras Ocidentais")or(r=="Terras da Coroa"):
	if	(r=="Norte"):
		print ("Snow")
	elif	(r=="Vale"):
		print ("Stone")
	elif	(r=="Terras Fluviais"):
		print ("Rivers")
	elif	(r=="Terras da Tempestade"):
		print ("Strom")
	elif	(r=="Dorne"):
		print ("Sand")
	elif	(r=="Ilhas de Ferro"):
		print ("Pyke")
	elif	(r=="Campina"):
		print ("Flowes")
	elif	(r=="Terras Ocidentais"):
		print ("Hill")
	elif	(r=="Terras da Coroa"):
		print ("Waters")
else:
	print ("Entrada", r, "invalida")