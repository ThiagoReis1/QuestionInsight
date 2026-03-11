nasc= int(input("ano de seu nascimento: "))
paiz= input("B para brasil e R para reino unido: ").upper()

idade= 2023 - nasc

if idade >= 18 and paiz == "B":
	temp= idade - 18
	print("sim")
	print(temp)
	
elif idade >= 17 and paiz == "R":
	temp= idade - 17 
	print("sim")
	print(temp)
	
elif idade < 18 and paiz == "B":
	temp= 18 - idade
	print("nao")
	print(temp)
	

elif idade < 17 and paiz == "R":
	temp= 17 - idade
	print("nao")
	print(temp)
	
elif paiz not in ["B", "R"]:
	print("invalido")