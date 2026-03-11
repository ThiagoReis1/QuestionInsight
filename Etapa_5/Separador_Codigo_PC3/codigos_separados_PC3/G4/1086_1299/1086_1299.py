#UFAM
#Adriano Brito - 21555121
#AV 2 - qst 01

n1 = float(input("Digite a nota: "))
n2 = float(input("DIgite a nota: "))
n3 = float(input("Digite a nota: "))

media = ( n1 + n2 + n3) /3

if( media >= 7 ):
	print(round(media, 1))
	print("Aprovado")
else:
	print(round(media, 1))
	print("Reprovado")