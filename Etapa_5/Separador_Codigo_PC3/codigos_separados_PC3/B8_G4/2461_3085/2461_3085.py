pc = float(input("valor preco de custo: "))

if(pc <= 50):
	v = pc + (pc * 1)
	print(round(v, 2))
elif(50.01 <= pc <= 100):
	v = pc + (pc * 0.5)
	print(round(v, 2))
elif(100.01 <= pc <= 500):
	v = pc + (pc * 0.4)
	print(round(v, 2))
elif(pc > 500):
	v = pc + (pc * 0.3)
	print(round(v, 2))