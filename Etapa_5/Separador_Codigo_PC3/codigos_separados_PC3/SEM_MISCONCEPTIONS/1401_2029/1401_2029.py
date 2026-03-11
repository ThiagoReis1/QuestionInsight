ataque = input("ataque maritimo OU terrestre? ")
unidades = int(input("unidades a serem destruidas: "))

vis = int(unidades / 40)+1
dra = int(unidades / 150)+1

if (ataque == "maritimo") :
	print("Viserion")
	print(vis)
else :
	print("Drogon")
	print(dra)