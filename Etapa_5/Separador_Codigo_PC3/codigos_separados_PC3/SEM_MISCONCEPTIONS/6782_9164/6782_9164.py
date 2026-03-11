anonasc = int(input("Qual o ano e nascimento? "))
pais = input("Digite B para Brasil e E para os Estados Unidos: ")
ano = 2023

idade = ano - anonasc
if idade >= 18 and pais.upper() == "B":
	tempo = idade - 18
	print("sim")
	print(tempo)
elif idade < 18 and pais.upper() == "B":
	falta = (anonasc - ano) + 18
	print("nao")
	print(falta)
elif idade > 16 and pais.upper() == "E":
	tempo1 = idade - 16
	print("sim")
	print(tempo1)
elif idade < 16 and pais.upper() == "E":
	falta1 = (anonasc - ano) + 16
	print ("nao")
	print(falta1)
else: 
	print("invalido")
	
	