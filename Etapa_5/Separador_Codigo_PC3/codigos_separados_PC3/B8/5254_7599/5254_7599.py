preco = float(input("preco:"))
codigo = int(input("regiao:"))
if(codigo==1):
	venda = preco - (preco*(40/100)) + preco*(10/100)
	print(round(venda,2))
else:
	if(codigo==2):
		venda = preco -(preco*(40/100)) + preco*(8/100)
		print(round(venda,2))
	else:
		if(codigo==3):
			venda = preco -(preco*(40/100)) 
			print(round(venda,2))
		else:
			if(codigo==4):
				venda = preco -(preco*(40/100)) + preco*(2/100)
				print(round(venda,2))