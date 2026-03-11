conta = float(input("Consumo de agua: "))

a = (conta *3 + 30 )
b = (conta * 3.50 + 30)
if(conta < 10):
	print(round(a, 2))
	
else:
	print(round(b, 2))