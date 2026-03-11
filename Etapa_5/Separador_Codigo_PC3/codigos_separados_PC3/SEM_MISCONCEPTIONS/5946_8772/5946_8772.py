escolha = input()
qtde = int(input())
qtde_r = int(input())

if escolha.upper() == "P":
	preco = (4.5 * qtde) + (3. * qtde_r)
	print(round(preco,2))
else: 
	preco = (6. * qtde) + (3. * qtde_r)
	print(round(preco,2))