unidade=input("Digite a unidade C ou P:  ")
medida=float(input("Digite a unidade:  "))
if (unidade=="C"):
	valor=(0.393701*medida)
	print(round(valor, 2))
else:
	cent=(medida/0.393701)
	print(round(cent, 2))