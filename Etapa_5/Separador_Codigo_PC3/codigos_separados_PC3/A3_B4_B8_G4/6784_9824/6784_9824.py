ano = int(input('digite: '))
pais = input('pais: ').upper()

idade = 2023 - ano
if idade >= 18 and pais == "B":
	print("sim")
elif idade >= 21 and pais == "R":
	print("sim")
elif idade < 18 and pais == "B":
	print("nao")
elif idade < 21 and pais == "R":
	print("nao")

else:
	print("invalido")
	
if idade < 18 :
	tr = 18 - idade
	print("tr")
elif idade < 21 :
	tr1 = 21 - idade
	print("tr1")


