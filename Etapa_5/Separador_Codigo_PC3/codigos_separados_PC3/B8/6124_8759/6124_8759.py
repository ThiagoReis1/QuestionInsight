peso= float(input())

if peso >= 3000.0 and peso< 3400.0:
	total = peso * 0.8
	print(round(total, 1))
elif peso >=3400.0 and peso < 3900.0:
	total= peso * 1.3
	print(round(total, 1))
elif peso >=3900.0 and peso < 4100.0:
	total= peso * 2.1
	print(round(total, 1))
elif peso >= 4100.0:
	total = peso * 3.0
	print(round(total, 1))