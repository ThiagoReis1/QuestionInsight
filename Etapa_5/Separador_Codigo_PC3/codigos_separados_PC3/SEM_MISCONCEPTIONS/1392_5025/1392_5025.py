consumo = float(input("Consumo de agua: "))

if consumo == "0" :
	valor = 30
	print(valor)
elif consumo < 10 :
	valor2 = (consumo * 3) + 30
	print(round(valor2,2))
else :
	valor3 = (consumo * 3.5) + 30
	print(round(valor3,2))