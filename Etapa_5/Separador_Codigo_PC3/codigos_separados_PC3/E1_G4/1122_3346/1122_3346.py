s=input("sobrenome:")
if(s=="Snow" or s=="Stone" or s=="Rivers" or s=="Storm" or s=="Sand" or s=="Pyke" or s=="Flowers" or s=="Hill" or s=="Waters"):
	if(s=="Snow"):
		print("Norte")
	elif(s=="Stone"):
		print("Vale")
	elif(s=="Rivers"):
		print("Terras Fluviais")
	elif(s=="Storm"):
		print("Terras da Tempestade")
	elif(s=="Sand"):
		print("Dorne")
	elif(s=="Pyke"):
		print("Ilhas de Ferro")
	elif(s=="Flowers"):
		print("Campina")
	elif(s=="Hill"):
		print("Terras Ocidentais")
	else:
		print("Terras da Coroa")
else:
	print("Entrada",s,"invalida")