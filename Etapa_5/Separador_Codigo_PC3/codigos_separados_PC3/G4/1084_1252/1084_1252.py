#Patrick Chessmam - 21200931	
#Avaliacao 2
#Questão 1

#notas recebidas
n1 = float(input("Digite nota 1: "))
n2 = float(input("Digite nota 2: "))
n3 = float(input("Digite nota 3: "))
n4 = float(input("Digite nota 4: "))

media = float((n1 + n2 + n3+ n4)/4)
print (round((media),1))

if (media >= 6) :
	print ("Aprovado")

else:
	print("Reprovado")