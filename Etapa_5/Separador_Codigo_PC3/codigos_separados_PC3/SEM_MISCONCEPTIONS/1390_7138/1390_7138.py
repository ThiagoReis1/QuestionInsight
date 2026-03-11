cons = float(input("INFORME O CONSUMO DO CLIENTE:"))

if(cons<=100):
	total = cons*1.20
else:
	total = cons*1.40 + 25
	
print(round(total,2))