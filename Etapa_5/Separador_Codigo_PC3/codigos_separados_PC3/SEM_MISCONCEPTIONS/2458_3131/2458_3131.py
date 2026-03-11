preco = float(input("Produto sem desconto: "))
cod = int(input("Codigo da regiao: "))

if (cod == 1):
	frete = 10
	vv = (preco - preco * (40/100) + preco * (frete / 100))
elif (cod == 2):
	frete = 8
	vv = (preco - preco * (40/100) + preco * (frete / 100))
elif (cod == 3):
	frete = 0
	vv = (preco - preco * (40/100) + preco * (frete / 100))
else:
	frete = 2
	vv = (preco - preco * (40/100) + preco * (frete / 100))
	
print(vv)