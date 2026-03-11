#Universidade Federal do Amazonas
#Thais de Almeida Ferreira
#21553775
#30/06/2016



N1 = float(input("Qual a primeira nota?"))
N2 = float(input("Qual a segunda nota?"))
N3 = float(input("Qual a terceira nota?"))

media = ((N1 + N2 + N3) / 3)
if (media >= 5):
	print(round(media, 1))
	print("Aprovado")
else:
	print(round(media,1))
	print("Reprovado")