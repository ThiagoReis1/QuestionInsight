preco = float(input("PRECO: "))
codigo = int(input("CODIGO: "))

if(codigo == 1):
	v = (preco - preco * 0.40) + preco * (10/100)
elif(codigo == 2):
	v = (preco - preco * 0.40) + preco * (8/100)
elif(codigo == 3):
	v = (preco - preco * 0.40) + preco * (0/100)
elif(codigo == 4):
	v = (preco - preco * 0.40) + preco * (2/100)
print(round(v,2))