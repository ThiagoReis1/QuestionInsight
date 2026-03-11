variavel=input("C ou K")
valor_temp=float(input(""))

if(variavel=='C'):
	print(round(valor_temp+273.15,2))
else:
	print(round(valor_temp-273.15,2))