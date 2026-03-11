a = float(input("conta: "))

if(a <= 300):
	conta = a * 1.10
else:
	conta = a * 1.06
	
print(round(conta, 2))	