g = float(input(": "))

if(g<5000):
	print(round(g * 0.05, 2))
if(g>=5000):
	g = ((g * 0.04) + 60.0)
	print(round(g, 2))
