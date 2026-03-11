# Universidade Federal do Amazonas
# Luis Gustavo Cardoso 
# Avaliacao Parcial 02

nota1 = float(input(" Digite o valor da nota: "))
nota2 = float(input(" Digite o valor da nota: "))
nota3 = float(input(" Digite o valor da nota: "))
nota4 = float(input(" Digite o valor da nota: "))

media = ( nota1 + nota2 + nota3 + nota4 ) / 4

if media >= 5:
	print(round(media, 2))
	print("Aprovacao")
else:
	print(round(media, 2))
	print("Reprovacao")