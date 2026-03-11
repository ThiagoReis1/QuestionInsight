cm = float(input("Digite o conusmo por minuto: "))

if (cm <= 100.00):
	total = 1.20 * cm
else:
	total = 25.0 + (1.40 * cm)
print(round(total,2))
	