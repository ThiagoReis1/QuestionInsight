preco = float(input()) 
codigo = int(input())


desconto = (preco * 0.40)
if codigo == 1:
	frete = (preco * 0.10)
	print(frete)
	valor_venda = (preco - desconto) + frete
elif codigo == 2:
	frete = (preco * 0.08)
	valor_venda = (preco - desconto) + frete
elif codigo == 3:
	frete = 0
	valor_venda = (preco - desconto) + frete
else:
	frete = (preco * 0.02)
	valor_venda = (preco - desconto) + frete
	
print(round(valor_venda, 2))
