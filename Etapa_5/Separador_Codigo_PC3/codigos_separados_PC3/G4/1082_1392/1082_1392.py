#Uninersidade Federal do Amazonas
#Laborátorio de Computação
#Letícia do Nascimento CLímaco
#21600841

n1 = float(input("prova 1"))
n2 = float(input("prova 2"))
n3 = float(input("prova 3"))
n4 = float(input("prova 4"))
n5 = float(input("prova 5"))
media = (n1+n2+n3+n4+n5)/5

if(media >= 5):
	print(round(media, 1))
	print("Aprovado")
else:
	print(round(media, 1))
	print("Reprovado")