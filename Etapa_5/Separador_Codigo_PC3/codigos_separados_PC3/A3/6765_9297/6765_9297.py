ano_nasc = int(input("Ano de nascimento: "))
pais = input("B ou R: ").upper()

ano_de_consulta = 2023
BR = 18
RSS = 21

calculo = ano_de_consulta - ano_nasc 
anosapt = calculo - 18 
anosapt2 = calculo - 21
anosapt3 = 18 - calculo
anosapt4 = 21 - calculo

if pais == "B" and calculo >= 18:
	print("sim")
	print(anosapt)
elif pais == "B" and calculo < 18:
	print("nao")
	print(anosapt3)
elif pais == "R" and calculo >= 21:
	print("sim")
	print(anosapt2)
elif pais == "R" and calculo < 21:
	print("nao")
	print(anosapt4)
else:
	print("invalido")
	
	
	