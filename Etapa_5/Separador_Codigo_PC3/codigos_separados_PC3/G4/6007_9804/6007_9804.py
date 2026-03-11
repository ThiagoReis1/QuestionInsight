q = int(input("Quantidade de espigas de milho compradas: "))

if q >= 6:
	x = q * 1.50
else:
	x = q * 1.85
	
print(round(x,2))
