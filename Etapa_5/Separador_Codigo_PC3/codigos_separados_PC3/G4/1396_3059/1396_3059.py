x= float(input("numero pago:"))

if(x <=300.00):
	print(round(x+ x*10/100,2))
else:
	print(round(x+ x*6/100,2))