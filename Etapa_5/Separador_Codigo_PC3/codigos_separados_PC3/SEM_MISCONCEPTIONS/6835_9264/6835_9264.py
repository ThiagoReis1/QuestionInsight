from numpy import * 

compra = input("Digite uma sequencia de produtos(Biscoito=B, Cereais=C, Enlatados=E): ")
preco = 0

for i in range(len(compra)):
	if compra [i] == 'B':
		preco += 3.75
	if compra [i] == 'C':
		preco += 7.90
	if compra [i] == 'E':
		preco += 9.85
print(round(preco,2))