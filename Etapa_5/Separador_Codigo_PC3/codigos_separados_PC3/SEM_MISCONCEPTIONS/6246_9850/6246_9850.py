resultado = input("Resultado dos confrontos: ").upper()

cont = 1

while resultado != "X":
	resultado = input("Resultado dos confrontos: ").upper()
	if resultado == "A":
		cont = cont + 1
		resultado = input("Resultado dos confrontos: ").upper()
print(cont)