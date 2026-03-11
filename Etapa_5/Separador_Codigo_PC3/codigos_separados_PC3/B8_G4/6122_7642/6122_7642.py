x = float(input("valor:"))

if x < 17.5:
	xf = x + 0.8
elif 17.5 < x < 35.0:
	xf = x + 1.3
elif 35.0 < x < 50.0:
	xf = x + 2.1
elif x >= 50:
	xf = x + 3.0
	
print(xf)