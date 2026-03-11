#Karoline Costa
#30 de Junho de 2016
#Avaliacao2
#questao 2

n= int(input("Digite um numero: "))
n1 = round(n//1000 , 0)
n2= round( n1 % 1000  , 0)
no= (n1-n2)**4
A= n==no
if ( A ):
	print(" X atende a propriedade")
else:
	
	print(no)