var1 = float(input("consumo do cliente: "))
cons = 100
tax = 25
if(var1 <= 100):
	conta = (var1*1.20)
else:
	conta = ((var1*1.40) + tax)


print(round(conta,2))
	

