#Desconto na loja Super Art Market

from numpy import *

produto = array(eval(input("Valor do produto: ")))
desc = 0

for i in range(size(produto)):
	if (produto[i] > 50):
		desc = desc + produto[i]*0.08

print(round((sum(produto) - desc),2))
	