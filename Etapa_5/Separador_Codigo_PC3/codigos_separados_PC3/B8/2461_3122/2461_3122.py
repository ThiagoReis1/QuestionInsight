preco = float(input("Preco de custo: "))

if (preco <= 50):
	p = 100 / 100
	vf = (preco * p) + preco
	print(round(vf, 2))

elif (preco >= 50.00) and (preco <= 100):
	p = 50/100
	vf = (preco * p) + preco
	print(round(vf, 2))
	
elif (preco >= 100.00) and (preco <= 500):
	p = 40/100
	vf = (preco * p) + preco
	print(round(vf, 2))
	
elif (preco >= 500):
	p = 30/100
	vf = (preco * p) + preco
	print(round(vf, 2))


	

	