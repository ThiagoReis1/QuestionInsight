#Cara ou Coroa

moeda = input("Cara ou Coroa? ")

cont = 0

cara = 0

while((moeda.upper() == "CARA") or (moeda.upper() == "COROA")):
	cont = cont + 1
	if(moeda.upper() == "CARA"):
		cara = cara + 1
	moeda = input("Cara ou Coroa? ")
	if(moeda.upper() == "S"):
		porc = (cara * 100) / cont
		print(cont)
		print(round(porc,2))
		