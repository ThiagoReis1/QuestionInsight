qtd = int(input("qtd de combustivel comum: "))

if qtd < 17.5 and qtd > 0:
	c = qtd + 0.8

elif qtd >= 17.5 and qtd <= 35:
	c = qtd + 1.3
	
elif qtd >= 35.0 and qtd <= 50.0:
	c = qtd + 2.1
	
else:
	c = qtd + 3.0
	
print(round(c, 1))