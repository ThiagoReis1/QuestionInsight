combustivel = float(input())

if combustivel < 17.5:
	total = combustivel + 10.5
	print(round(total, 1))
	
elif combustivel >= 17.5 and combustivel < 35:
	total = combustivel + 14
	print(round(total, 1))
	
elif combustivel >= 35 and combustivel < 50:
	total = combustivel + 18.6
	print(round(total, 1))
	
else:
	total = combustivel + 24.5
	print(round(total, 1))