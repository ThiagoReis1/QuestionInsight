sa = float(input(" salario atual: "))

if (sa < 1212.00):
	x = sa + (sa * 0.12)
elif (sa >= 1212.00) and (sa <= 5000.00):
	x = sa + (sa * 0.08)
else:
	x = sa + (sa * 0.03)
print(round(x, 2))