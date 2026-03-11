TV = float(input("digite o valor: "))
if(TV<=200):
	msg = 5000 + (100 * TV)
else:	
	msg = 8000 + (100 * 200) + 90 * (TV - 200)
print(round(msg, 2))	
