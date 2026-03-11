hr = float(input("horas trabalhadas: "))

p1 = (50 * hr) + 500
p2 = (60 * hr) + 600
p3 = (70 * hr) + 700
p4 = (80 * hr) + 800

if (hr <= 10):
	print(round(p1, 2))
elif (hr > 10 and hr <= 20):
	print(round(p2, 2))
elif (hr > 20 and hr <= 30):
	print(round(p3, 2))
elif (hr > 30 ):
	print(round(p4, 2))