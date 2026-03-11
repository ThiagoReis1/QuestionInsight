tipo_de_ataque = input("Maritimo ou terrestre: ")
tipo_de_ataque = tipo_de_ataque.lower()
bafo = int(input("Quantas baforadas: "))

if(tipo_de_ataque == "maritimo"):
	dragao = "Viserion"
	destruido = bafo * 40
	print(dragao)
	print(destruido)
	
elif(tipo_de_ataque == "terrestre"):
	dragao = "Drogon"
	destruido = bafo * 150
	print(dragao)
	print(destruido)
	
