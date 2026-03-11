consumo = int(input("Consumo de agua: "))
taxa = 20
if(consumo < 10):
	conta = round(taxa + 2 * consumo, 2)
	print(conta)
elif(consumo>= 10 and consumo < 20):
	conta = round(taxa + 2.5 * consumo, 2)
	print(conta)
elif(consumo >= 20 and consumo < 40):
	conta= round(taxa + 2.75 * consumo, 2)
	print(conta)
elif(consumo >= 40):
	conta = round(taxa + 3 * consumo, 2)
	print(conta)