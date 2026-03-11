val = float(input("Valor da compra:"))
op = input("Opcao de pagamento:")

if (op.upper() == 'C'):
	qual = int(input("1 ou 2:"))
	if (qual == 1):
		print(round(val,2))
	else:
		cal = val + val*0.07
		print(round(cal,2))
		
elif (op.upper() == 'D'):
	cal = val*0.88
	print(round(cal,2))
	
elif (op.upper() == 'P'):
	cal = val*0.88
	print(round(cal,2))