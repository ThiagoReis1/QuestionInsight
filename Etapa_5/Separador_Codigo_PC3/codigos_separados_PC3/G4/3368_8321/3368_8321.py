t = input("C ou K?: ")
temp = float(input("temperatura"))

if (t == "C"):
	x = temp + 273.15
else:
	x = temp - 273.15
print(round(x ,2))
