# faça seu código aqui!
d = int(input("Dias de aluguel: "))
v = 100.00

if d < 7:
	total = v * d + 15.00
elif	d == 7:
	total = v * d + 12.00
else:
	total = v * d + 10.00
print(round(total,2))