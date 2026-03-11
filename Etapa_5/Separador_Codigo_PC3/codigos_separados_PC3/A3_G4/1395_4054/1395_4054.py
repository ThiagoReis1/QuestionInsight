vd = float(input(""))
if (vd <= 1000):
	t = 0.05 * vd
if (vd > 1000):
	t = 0.05 * 1000 + 0.1 * (vd - 1000)
print(round(t, 2))