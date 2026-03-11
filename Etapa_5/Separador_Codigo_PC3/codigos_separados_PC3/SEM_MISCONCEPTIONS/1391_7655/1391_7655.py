consumo= float(input("Digite o consumo: "))
if (consumo<=150):
	conta= consumo*0.60+5
	print(round(conta,2))
else:
	conta= consumo*0.75+16
	print(round(conta, 2))
