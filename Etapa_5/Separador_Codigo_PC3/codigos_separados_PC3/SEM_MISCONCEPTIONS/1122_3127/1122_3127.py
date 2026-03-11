sobrenome = str(input("digite o sobrenome:"))
a = str(sobrenome.upper())

if(a == "SNOW" ):
	print("Norte")
elif(a == "STONE"):
	print("Vale")
elif(a == "RIVERS"):
	print("Terras Fluviais")
elif(a == "STORM"):
	print("Terras da Tempestade")
elif(a == "SAND"):
	print("Dorne")
elif(a == "PYKE"):
	print("Ilhas de Ferro")
elif(a == "FLOWERS"):
	print("Campina")
elif(a == "HILL"):
	print("Terras Ocidentais")
elif(a == "WATERS"):
	print("Terras da Coroa")
else:
	print("Entrada ",sobrenome," invalida")