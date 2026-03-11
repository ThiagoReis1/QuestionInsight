
min = float(input("Digite o valor: "))

if (min <= 200):
	Total = 5000 + min * 100
	print(round(Total, 2))
else:
	minex = min - 200.0
	Total1 = 90.0 * minex
	Total2 = Total1 + 8000.0
	Total3 = 100.0 * 200.0
	Total4 = Total2 + Total3
	print(round(Total4, 2))