a = float(input("valor consumido? "))
#
if (a <= 300):
	g = (a * 10) / 100
	print(round(a + g , 2))
else:
	m = (a * 6) / 100
	print(round(m + a , 2))