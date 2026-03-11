##Refeicao

prato = int(input("Numero do prato: "))
sobremesa = int(input("Numero da sobremesa: "))
bebida = int(input("Numero da bebida: "))

#condicao

#prato 
if (prato == 1):
	cal = 180
elif (prato == 2):
	cal = 230
elif (prato == 3):
	cal = 250
else:
	cal = 350
	
print(cal)

if (sobremesa == 1):
	ca = 75
elif (sobremesa == 2):
	ca = 110
elif (sobremesa == 3):
	ca = 170
else:
	ca = 200
	
print(ca)

if (bebida == 1):
	c = 20
elif (bebibda == 2):
	c =