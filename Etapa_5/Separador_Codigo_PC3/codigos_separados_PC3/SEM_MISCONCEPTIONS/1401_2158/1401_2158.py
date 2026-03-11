tda = input("nome: ").lower()
qdu = int(input("Valor: "))

Viserion = 40
Drogon = 150

obj1 = (qdu//Viserion + 1)
obj2 = (qdu//Drogon + 1)
if (tda == "maritimo" ):
	print("Viserion")
	print(obj1)
else:
	print("Drogon")
	print(obj2)
	
