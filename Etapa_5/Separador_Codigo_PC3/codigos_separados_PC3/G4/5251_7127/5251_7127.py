c = input("Cidade Destino: ")
y = int (input("Idade: "))

print("Entradas: ", c, ",", y)

if(c == "porto velho"):
	t = 500.00
elif(c == "santarem"):
	t = 370.00
elif(c == "belem"):
	t = 600.00
elif(c == "tefe"):
	t = 360.00
elif(c == "tabatinga"):
	t = 550.00
else:
	print("entradas invalidas")
if(2 < y):
	print(c == t * 0)