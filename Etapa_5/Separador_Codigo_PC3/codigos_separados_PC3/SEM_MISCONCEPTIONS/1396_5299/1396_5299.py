consumo = float(input())
if (consumo <= 300):
	g = consumo + consumo*0.1
	print(round(g,2))
else:
	h = consumo + consumo*0.06
	print(round(h,2))