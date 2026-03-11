t=float(input())
if t < 50:
	v = 4.50 + 60
elif t == 50:
	v = 5.50 + 60
else:
	v = 6.50 + 60
print(round(v,2))
