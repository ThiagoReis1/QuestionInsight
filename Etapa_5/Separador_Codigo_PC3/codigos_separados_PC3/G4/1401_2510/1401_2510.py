tipo = input("Tipo de Ataque: ")

a = int(input("Número de embarcações ou guerreiros: "))

m = 40

t = 150

if (tipo == "maritimo"):
	if ( a % m == 0):
		x = a / m
		print("Viserion")
		print(int(x))
	else:
		x = (a // m) + 1
		print("Viserion")
		print(int(x))
else:
	if ( a % t == 0):
		x = a / t
		print("Drogon")
		print(int(x))
	else:
		x = (a // t) + 1
		print("Drogon")
		print(int(x))