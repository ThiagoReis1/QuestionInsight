# Lizandra Kamila Muniz de Andrade - 21553759
# Universidade Federal do Amazonas - UFAM
# Faculdade de Tecnologia - FT
# 07.07.2016
n1 = float(input("insira a primeira nota: "))
n2 = float(input("insira a segunda nota: "))
n3 = float(input("insira a terceira nota: "))
n4 = float(input("insira a quarta nota: "))
n5 = float(input("insira a quinta nota: "))
media = (n1 + n2 + n3 + n4 + n5) / 5
if (media>= 7):
	print (round(media, 2))
	print ("Aprovacao")
else:
	print (round(media, 2))
	print ("Reprovacao")
	
