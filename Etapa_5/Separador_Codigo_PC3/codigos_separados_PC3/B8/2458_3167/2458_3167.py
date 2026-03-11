preco = float(input("digite o valor do produto: "))
cod = float(input("codigo da regiao: "))
a = 10
b = 8
c = 2
if(cod == 1):
	valor_da_venda = (preco-(preco*0.4)) + (preco*(a/100))
	print(round(valor_da_venda, 2))
elif(cod == 2):
	valor_da_venda = (preco-(preco*0.4)) + (preco*(b/100))
	print(round(valor_da_venda, 2))
elif(cod == 3):
	valor_da_venda = (preco-(preco*0.4)) 
	print(round(valor_da_venda, 2))
elif(cod == 4):
	valor_da_venda = (preco-(preco*0.4)) + (preco*(c/100))
	print(round(valor_da_venda, 2))


