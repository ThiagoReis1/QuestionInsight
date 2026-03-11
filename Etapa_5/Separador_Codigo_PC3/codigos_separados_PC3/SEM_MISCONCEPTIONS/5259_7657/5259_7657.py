mensalidade = float(input(":"))
crianca = int(input(":"))
if crianca == 1:
	x = (mensalidade - (mensalidade * 10/100)) * crianca
	print(round(x, 2))
if crianca == 2:
	x = (mensalidade -(mensalidade * 30/100)) * crianca
	print(round(x, 2))
if crianca >= 3:
	x = (mensalidade - (mensalidade * 40/100)) * crianca
	print(round(x, 2))