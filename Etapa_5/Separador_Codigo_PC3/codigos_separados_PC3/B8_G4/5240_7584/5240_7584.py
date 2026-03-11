a = int(input("Qual o comsumo de energia? "))

if (a > 100):
	m = a * 0.5 + 50
elif (a >= 100 and a < 250):
	m = a * 0.75 + 50
elif (a >= 250 and a <500):
	m = a * 1 + 50
elif (a >= 500):
	m = a * 1.25 + 50

print(round(m, 2))