nasc = int(input("digite o ano de nascimento: "))
pais = input("digite B ou R: ")
	
if (2023 - nasc >= 18) and pais == "R":
	print("sim")
	apto = (2023 - nasc) - 18
	print(apto)
		
elif (2023 - nasc < 21) and pais.upper() == "B":
	print("nao")
	apto = 21 - (2023 - nasc)
	print(apto)
		
elif (2023 - nasc < 18) and pais == "R":
	print("nao")
	apto = 18 - (2023 - nasc)
	print(apto)

elif (2023 - nasc >= 21) and pais.upper() == "B":
	print("sim")
	apto = (2023 - nasc) - 21
	print(apto)
else:
	print("invalido")