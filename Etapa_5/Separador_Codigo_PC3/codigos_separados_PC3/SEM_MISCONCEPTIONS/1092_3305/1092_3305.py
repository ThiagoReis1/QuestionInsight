from math import *
numero = int(input("entre com o numero fornecido: "))
d1=numero//100
d2=(numero%100)//10
d3=numero%10
calculo = (d1**3) + (d2**3) + (d3**3)
if(numero == calculo):
	mensagem = "atende"
else:
	mensagem = "nao atende"
print(numero)
print(mensagem)
