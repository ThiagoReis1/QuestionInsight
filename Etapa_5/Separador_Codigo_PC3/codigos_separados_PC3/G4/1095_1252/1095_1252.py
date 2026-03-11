#Patrick Chessmam - 21200931	
#Avaliacao 2
#Questão 2

x = int(input("Digite um numero: "))

if (x == (x // 10000) + (x % 10000)**2 ) :
	print ("X atende a propriedade")
	
else:
	print((x // 10000) + (x % 10000)**2 )