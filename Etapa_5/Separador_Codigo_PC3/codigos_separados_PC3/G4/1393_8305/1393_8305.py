p= float(input())


if (p >= 5000):
	t = (p * 0.04) + 60
else:
	t = p * 0.05
print(round(t,2))