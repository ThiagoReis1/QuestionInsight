p = float(input("digite o peso em gramas: "))

if (p < 5000):
	f = 0.05*p
	print("", round(f,2))
else:
	f = 60 + (0.04*p)
	print("", round(f,2))