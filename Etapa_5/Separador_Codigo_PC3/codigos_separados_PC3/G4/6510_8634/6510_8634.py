# faça seu código aqui!
dia = input("Dia da semana: ")
qnt = int(input("Quantidade de pratos consumidos pelo cliente: "))
pag = qnt*22.0

if dia == "qua":
	total = pag - (pag*0.15)
	print(round(total, 2))
else:
	print(round(pag, 2))