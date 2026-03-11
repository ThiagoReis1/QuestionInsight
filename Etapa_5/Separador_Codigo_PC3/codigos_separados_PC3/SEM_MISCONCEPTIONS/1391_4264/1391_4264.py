consumo = float(input("consumo de energia:"))
if (consumo <= 150):
	conta = round((consumo * 0.6) + 5, 2)
else:
	conta = round((consumo * 0.75) + 16, 2)
print(conta)