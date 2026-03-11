prova_1 = float(input("digite a  nota 1:"))
prova_2 = float(input("digite a  nota 2:"))
prova_3 = float(input("digite a  nota 3:"))
prova_4 = float(input("digite a  nota 3:"))
media = (prova_1 + prova_2 + prova_3 + prova_4) / 4

if (media >= 7.0):
	print (round(media,2))
	print ("Aprovado")
else:
	print (round(media,2))
	print ("Reprovado")