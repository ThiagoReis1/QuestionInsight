ano = int(input("sua data de nascimento: "))
pais = input("digite a inicial do seu pais: ")

if(pais.upper() == "B") and (2023 - ano >= 18):
	print("sim")
	print(2023 - (ano + 18))
	
elif(pais.upper() == "E") and (2023 - ano >= 16):
	print("sim")
	print(2023 - (ano + 16))
	
elif(pais.upper() == "B") and (2023 - ano < 18):
	print("nao")
	print(18 - (2023 - ano))
	
elif(pais.upper() == "E") and (2023 - ano < 16):
	print("nao")
	print(16 - (2023 - ano))

else:
	print("invalido")