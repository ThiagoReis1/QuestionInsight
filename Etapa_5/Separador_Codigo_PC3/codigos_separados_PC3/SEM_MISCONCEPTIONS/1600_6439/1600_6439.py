from numpy import *

preco = array(eval(input("entre com o valor da compra: ")))
desconto = 0
i = 0 

while (i < size(preco)):
	if (preco[i] > 80):
		desconto = desconto + preco[i] * 0.15
	i = i + 1

print(round(sum(preco)-desconto, 2))



