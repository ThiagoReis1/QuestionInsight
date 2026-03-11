preco = float(input("preco"))
opc = input("d para dinheiro, p para pix e c para cartao (D/P/C)")

if opc.upper() == "C":
	c1c2 = int(input("1 para parcelar em 1 vez e 2 para duas"))
	if c1c2 == 1:
		pf = preco
		print(round(pf,2))
	elif c1c2 == 2:
		pf = preco + preco*0.07
		print(round(pf,2))

elif opc.upper() == "D":
	pf = preco - preco*0.18
	print(round(pf,2))

if opc.upper() == "P":
	pf = preco - preco*0.18
	print(round(pf,2))