a= float(input("Consumo de minutos: "))

if a <= 100 :
	msg = (a * 1.20)
	
else:
	msg= (25 + (a * 1.40))
	
print(float(round(msg,2)))