dias = float(input("dias reservados: "))


if dias < 15:
	total = 175 * dias + 20
elif dias == 15:
	total = 175 * dias + 16
else:
	total = 175 * dias + 10
print(round(total, 2))