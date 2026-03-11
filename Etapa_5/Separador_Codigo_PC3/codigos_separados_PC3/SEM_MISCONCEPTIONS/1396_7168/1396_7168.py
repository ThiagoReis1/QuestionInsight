cons = float(input("Qual o consumo: "))
if(cons <= 300):
	pagar_1 = cons * 0.1
else:
	pagar_1 = cons * 0.06
total = cons + pagar_1	
print(round(total, 2))