destino = int(input("Cidade de destino: "))
idade = int(input("Idade do passageiro: "))

if (idade <= 2):
	x = destino * 500.00
	print(x)
elif(idade >= 3):
	x = destino * 370.00 
	print(x)
	