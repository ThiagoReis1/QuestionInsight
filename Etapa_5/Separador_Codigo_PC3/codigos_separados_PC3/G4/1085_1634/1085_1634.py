#Simony Batista Lima     Matricula: 21650621
#14/07/2016 Prova 02


P1= float(input("Digite a nota da P1: "))
P2= float(input("Digite a nota da P2: "))
P3= float(input("Digite a nota da P3: "))
P4= float(input("Digite a nota da P4: "))
P5= float(input("Digite a nota da P5: "))

media = (P1 + P2 + P3 + P4 + P5) / 5

if(media >= 6):
	print(round(media,2))
	print("Aprovado")

else:
	print(round(media,2))
	print("Reprovado")