v = float(input())

if (v > 300):
	g = v * 0.06
else:
	g = v * 0.1

vt = v + g
print(round(vt, 2))