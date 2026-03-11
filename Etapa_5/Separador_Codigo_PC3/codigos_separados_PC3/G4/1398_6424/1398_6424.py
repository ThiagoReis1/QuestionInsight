t = float(input())
if t<= 200:
	v = 5000 + t * 100
else:
	v = 8000 + 100 * 200 + 90 * (t - 200)
print(round(v,2))