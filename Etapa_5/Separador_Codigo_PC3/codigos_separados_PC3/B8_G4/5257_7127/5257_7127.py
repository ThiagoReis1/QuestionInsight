x = float(input("Preco de custo: "))

if(x <= 50.00):
	print(round(x+x, 2))
elif(50.01 <= x <= 100.00):
	print(round(x + x/2, 2))
elif(101.01 <= x <= 500.00):
	print(round(x + x*40/100, 2))
elif(x > 500.00):
	print(round(x + x*30/100, 2))
