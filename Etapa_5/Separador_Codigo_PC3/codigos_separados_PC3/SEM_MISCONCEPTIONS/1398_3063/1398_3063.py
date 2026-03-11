temp = float(input("digite o tempo de voo"))

n1 = temp - 200

calc1 = 5000 + 100 * temp
calc2 = 8000 + 100 * 200 + (90 * n1)

if (temp >= 200):
	print(round(calc2,2))
else:
	print(round(calc1,2))