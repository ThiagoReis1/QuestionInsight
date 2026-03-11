# Universidade Federal do Amazonas
# Jessica da Fonseca Correa - 21600613
# Avaliacao 2
# 07/07/2016

nota1 = float(input("Insira a primeira nota"))
nota2 = float(input("Insira a segunda nota"))
nota3 = float(input("Insira a terceira nota"))

media = (nota1 + nota2 + nota3) / 3

if(media >= 5.0):
	print(round(media, 1))
	print("Aprovado")
			
else:
	print(round(media, 1))
	print("Reprovado")