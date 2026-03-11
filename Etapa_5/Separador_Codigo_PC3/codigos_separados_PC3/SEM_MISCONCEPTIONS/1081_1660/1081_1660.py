####################################
# Universidade Federal do Amazonas
# Mauricio Naoto Handa Mitoso
# 30/06/2016
####################################

#entrada das notas
nota1 = float(input("Qual a primeira nota? "))
nota2 = float(input("Qual a segunda nota? "))
nota3 = float(input("Qual a terceira nota? "))
nota4 = float(input("Qual a quarta nota? "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(round(media, 2))
if (media >= 5.0):
	print ("Aprovacao")
if (media <= 5.0):
	print ("Reprovacao")
