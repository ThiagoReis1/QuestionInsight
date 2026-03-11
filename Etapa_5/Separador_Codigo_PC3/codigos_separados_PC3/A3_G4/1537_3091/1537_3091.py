from math import*
x=float(input("digite numero: ")) 
k=int(input("digite numero inteiro: ")) #quantidade de termos da serie

i=1
ack=1.0
imp=0

while(k>i): #enquanto o numero x for maior que o num de termos da serie faça a serie
	termo = (x**(i)/factorial(i)) #termo geral
	i = i + 1
	ack = ack+termo
	
	
print(round(ack, 9))