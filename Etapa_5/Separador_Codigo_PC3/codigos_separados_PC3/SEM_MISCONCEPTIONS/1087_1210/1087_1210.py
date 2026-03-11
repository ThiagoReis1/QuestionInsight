# UNIVERSIDADE FEDERAL DO AMAZONAS
# PHILIPPE DA SILVA SOARES
# MATRICULA:21650892

nota_um=float(input("informe a nota 1: "))
nota_dois=float(input("informe a nota 2: "))
nota_tres=float(input("informe a nota 3: "))
nota_quatro=float(input("informe a nota 4: "))

media=(nota_um + nota_dois + nota_tres + nota_quatro)/4

if (media >=7 ):
		print(round(media,2))
		print("Aprovado")
else:
	print(round(media,2))
	print("Reprovado")