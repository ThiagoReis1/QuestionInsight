milho = int(input("milhos: "))
milhonormal = milho * 1.85
milhopromo = milho * 1.50
if milho > 6:
	print(round(milhopromo, 2))
else:
	print(round(milhonormal, 2))
	
