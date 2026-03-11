# Rodrigo de Oiveira Brasil Ferreira - 21602328
# Avaliacao 2 - grupo 2
# 14 / 07 / 2016
# Entrada
n1 = float(input("digite a nota 1:"))
n2 = float(input("digite a nota 2:"))
n3 = float(input("digite a nota 3:"))

media = (n1 + n2 + n3) / 3
print(round(media, 1))

if(media >= 7):
	print("Aprovado")
else:
	print("Reprovado")
			  