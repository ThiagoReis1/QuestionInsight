#Universidade Federal do Amazonas - UFAM
#Igor Rodrigues Chicolet da Silva - 21204615
#29/06/2016

n1 = float(input("Qual a nota 1? "))
n2 = float(input("Qual a nota 2? "))
n3 = float(input("Qual a nota 3? "))
n4 = float(input("Qual a nota 4? "))

media_arit = (n1 + n2 + n3 + n4) / 4
print(round(media_arit,2))
if(media_arit >= 7):
	print("Aprovado")
else:
	print("Reprovado")