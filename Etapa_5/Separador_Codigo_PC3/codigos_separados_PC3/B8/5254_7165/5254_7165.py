preco = float(input("Preco do produto sem desconto: "))
codigo = int(input("Codigo da regiao de entrega: "))
dbf = 0.4 * preco
if(codigo == 1):
	valor_da_venda = round((preco - dbf) + preco * 0.1, 2)
	print(valor_da_venda)
elif(codigo == 2):
	valor_da_venda = round(preco - dbf + preco * 0.08, 2)
	print(valor_da_venda)
elif(codigo == 3):
	valor_da_venda = round(preco - dbf, 2)
	print(valor_da_venda)
elif(codigo == 4):
	valor_da_venda = round(preco - dbf + preco *0.02, 20)
	print(valor_da_venda)
	