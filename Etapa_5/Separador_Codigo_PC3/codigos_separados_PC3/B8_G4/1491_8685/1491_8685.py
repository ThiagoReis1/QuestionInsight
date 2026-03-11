
peso = int(input())

if peso >= 0 and peso <= 5000:
	t = 0.03
	tx = 20
elif peso > 5001 and peso <= 6000:
	t = 0.04
	tx =25.00 
elif peso>6001 and peso<= 7000:	
	t=0.05
	tx=30
elif peso>7000:
	t=0.06
	tx=35.00
	
valor=peso*t+tx
print(round(valor, 2))
	