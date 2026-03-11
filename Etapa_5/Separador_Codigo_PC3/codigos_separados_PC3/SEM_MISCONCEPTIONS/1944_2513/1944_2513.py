#Peso molecular
aminoacido = input("Digite o nome do aminoacido: ").lower()

O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

Leucina = (C*6)+(H*13)+(N*1)+(O*2)
Lisina = (C*6)+(H*15)+(N*2)+(O*2)

if(aminoacido == "leucina"):
	print(round(Leucina,2))
else:
	print(round(Lisina,2))


