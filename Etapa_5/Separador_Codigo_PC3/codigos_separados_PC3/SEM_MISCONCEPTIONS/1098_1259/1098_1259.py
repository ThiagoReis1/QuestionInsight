#Julia Pacheco
#30 de Junho de 2016
#Av 02 - Ex 02

#ler numero
num = int(input("numero: "))

#divide em partes
parte1 = num//1000
parte2 = num%1000

#calculo da potencia
valor = (parte1 - parte2)**4 

#faz o teste
if(valor == num):
	print(num, "atende a propriedade")
else:
	print(valor)