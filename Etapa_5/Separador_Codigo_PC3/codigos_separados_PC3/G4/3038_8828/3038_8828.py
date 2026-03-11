from math import*

x = float(input("f de x: "))

if (x<=(-1)) or (x>=1):
	f = abs((x**(1/2)))
	print(round(f, 2))

elif x == 0:
	print(round("0", 2))
else:
	f = abs(x)
	print(round(f, 2))
