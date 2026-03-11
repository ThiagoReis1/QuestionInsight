x = int(input("informe a quantidade de dias"))

if x < 15:
	total = x * 175 + 20
elif x == 15:
	total = x * 175 + 16
else:
	total = x * 175 + 10
print(round(total, 2))