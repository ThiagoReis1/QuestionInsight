nasc = int(input("insira o ano de nascimento: "))
pais = input("digite o pais: ").upper()

ano = 2023

if pais == "B":
	if ano - nasc >= 21:
		print("sim")
		print(ano - nasc - 21)
	
elif pais == "E":
	if ano - nasc >= 18:
		print("sim")
		print ( ano - nasc - 18)

if pais != "B" and pais != "E":
	print("invalido")
	

	


		
	