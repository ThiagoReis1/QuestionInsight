var = float(input("Qual o valor consumido? "))

cal1 = var*0.1
cal2 = var*0.06

if (var > 300):
	conta1 = var + cal2
	print(round(conta1,2))
else:
	conta2 = var + cal1
	print(round(conta2,2))