preco = float(input("Qual o preco do produto sem desconto: "))
codigo = int(input("Qual o codigo da regiao: 1, 2, 3 ou 4? "))

if (codigo == "1"):
	v = preco - preco * 0.40 + preco * 10/100
	print(v, 2)
elif (codigo == "2"):
	v = preco - preco * 0.40 + preco * 8/100
	print(v, 2)
elif (codigo == "3"):
	v = preco - preco * 0.40 + preco * 0
	print(v, 2)
elif (codigo == "4"):
	v = preco - preco * 0.40 + preco * 2/100
	print(v, 2)