bs = input("Bolo ou Salgado?")
qntd_bs = int(input("Quantidade de bolo ou salgado?"))
qntd_cap = int(input("Quantidade de capucchino?"))
if bs=="B":
	conta = (qntd_bs*5)+(qntd_cap*7.50)
	print(conta)
else:
	conta = (qntd_bs*4)+(qntd_cap*7.50)
	print(conta)