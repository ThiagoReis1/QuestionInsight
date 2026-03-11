s = float(input("digite seu salario: "))

if (s < 1212):
	t = s * 0.12 + s
	print(round(t, 2))
elif(s >= 1212) and (s <= 5000):
	t = s * 0.08 + s
	print(round(t, 2))
else:
	t = s * 0.03 + s
	print(round(t, 2))