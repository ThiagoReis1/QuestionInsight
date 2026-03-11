consumo = float(input())
taxa = 30
if consumo<10:
	total = consumo * 3 + taxa
else:
	total = consumo * 3.5 + 30
print(total)