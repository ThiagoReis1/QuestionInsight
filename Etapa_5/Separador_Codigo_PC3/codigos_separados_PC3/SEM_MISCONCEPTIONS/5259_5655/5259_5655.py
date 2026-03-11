mens = float(input("PRECO DA MENSALIDADE: "))
kid= int(input("NUMERO DE CRIANCAS: "))

if(kid >= 3):
	total = (mens * kid) - (mens * 0.4) * kid
	print(round(total, 2))
elif(kid == 2):
	total = (mens * kid) - (mens * 0.3) * kid
	print(round(total, 2))
elif(kid == 1):
	total = (mens * kid) - (mens * 0.1) * kid
	print(round(total, 2))
else:
	print(round(mens, 2))