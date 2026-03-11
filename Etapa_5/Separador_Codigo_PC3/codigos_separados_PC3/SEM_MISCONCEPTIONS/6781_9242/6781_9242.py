ano_nasc = int(input("ano de nascimento: "))
pais = input("B ou E: ").upper()

ano_de_consulta = 2023

calculo = ano_de_consulta - ano_nasc
anosap = calculo - 18
anosap2 = calculo - 21
anosap3 = 18 - calculo
anosap4 = 21 - calculo

if pais == "E" and calculo >= 18:
	print("sim")
	print(anosap)
elif pais == "E" and calculo < 18:
	print ("nao") 
	print(anosap3)
elif pais == "B" and calculo >= 21:
	print("sim")
	print(anosap2)
elif pais == "B" and calculo < 21:
	print("nao")
	print(anosap4)
else:
	print("invalido")
		
		
		