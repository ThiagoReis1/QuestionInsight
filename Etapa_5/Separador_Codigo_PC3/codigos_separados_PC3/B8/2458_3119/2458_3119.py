preco = float(input("Preco do produto: "))
codigo = input("Codigo da regiao: ")

if (codigo == "1"):
   print(preco - preco * (40/100) + preco * (10/100))
elif (codigo == "2"):
	print(preco - preco * (40/100) + preco * (8/100))
elif (codigo == "3"):
	print(preco - preco * (40/100) + preco * (0/100))
elif (codigo == "4"):
   print(preco - preco * (40/100) + preco * (2/100))	

