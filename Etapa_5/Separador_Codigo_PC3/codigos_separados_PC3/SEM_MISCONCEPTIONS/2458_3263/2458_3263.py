preco = float(input("qual preco: "))
cod = int(input("qual codigo: "))

descBF = 0.40

if(cod == 1):
	frete = 0.10 * preco
elif(cod == 2):
	frete = 0.08 * preco
elif(cod == 3):
	frete = 0.00 * preco
elif(cod == 4):
	frete = 0.02 * preco

else:
	print("nao houve venda")
	
valodavenda = (preco - preco * descBF) + preco * (frete / 100)

print(valodavenda)