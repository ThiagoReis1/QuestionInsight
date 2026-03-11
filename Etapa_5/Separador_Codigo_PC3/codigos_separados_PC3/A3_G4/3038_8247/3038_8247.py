from math import*
x = float(input("numero: "))
w = 0
y = 0
if x >= 1 or x <= -1:
	w = abs(x)
	y = sqrt(w)
	print(round(y, 2))
elif -1 < x < 0 or 0 < x < 1:
	w = abs(x)
	print(round(w, 2))
else:
	print("0")