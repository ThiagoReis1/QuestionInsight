escala = input("C ou K: ")
t = float(input())
if (escala == "C"):
	a = t + 273.15
	print(round(a,2))
else:
	b = t - 273.15
	print(round(b,2))