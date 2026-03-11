#Descontao na loja
from numpy import *

item = array(eval(input("Digite o total da sua compra: ")))

#condicao 
i = 0
desc = 2.50
total = 0


while (i < size(item)):
	if (item[i] > 40):
		total = total + item[i] - desc
	else:
		total = total + item[i]
	i = i + 1
	
print(total)
