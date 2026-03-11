peso=float(input("peso da encomenda em gramas: "))

if(peso< 5000.0):
	valor=(peso*0.05)
	print(round(valor,2))

else:
	valor=(peso*0.04)+60
	print(round(valor,2))