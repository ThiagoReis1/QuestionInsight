qntl = int(input("quantidade de laranjas"))
if qntl >= 6 :
	preco = qntl*0.6
	print(round(preco,2))
else:
	preco = qntl*0.75
	print(round(preco,2))