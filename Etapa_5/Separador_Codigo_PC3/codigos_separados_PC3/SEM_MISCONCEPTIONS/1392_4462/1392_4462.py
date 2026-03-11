consumo = float(input("digite o valor: "))
taxa = 30
if(consumo>=10):
	total = consumo*3.50 + taxa 
else:
	total = consumo*3 + taxa 
print(round(total,2))
