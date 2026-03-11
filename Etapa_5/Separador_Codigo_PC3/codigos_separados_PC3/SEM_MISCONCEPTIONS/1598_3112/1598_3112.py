from numpy import*

#entrada
vetor = array(eval(input("Valor do custo dos itens: ")))

#Variavel do desconto
desconto = 0

for i in range(vetor):
	if( i > 80):
		desconto = desconto + 5
		
#total de compras
total = sum(vetor)

#total de compras com desconto
soma = total - desconto
print(soma)
		
	