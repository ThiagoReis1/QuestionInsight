cons = int(input('Consumo de agua: '))
taxa = 30

if (cons >= 10):
	conta = (3.50 * cons) + taxa
	
else: 
	conta = (3.0 * cons) + taxa
	
print(round(conta, 2))
