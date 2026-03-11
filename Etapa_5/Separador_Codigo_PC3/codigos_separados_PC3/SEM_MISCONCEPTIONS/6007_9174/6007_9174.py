qntd = int(input("qnt de produtos: "))
if qntd<=6:
	 x = 1.85

else:
	x = 1.50
	
total = x * qntd

print(round(total,2))
