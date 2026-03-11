dd = int(input("Quandidade de duplas deliciosas: "))

conta = 32.90*dd
desconto = conta - conta*20/100
conta2 = dd * 32.90

if dd > 3:
	print(round(desconto,2))
else:
	print(round(conta2, 2))