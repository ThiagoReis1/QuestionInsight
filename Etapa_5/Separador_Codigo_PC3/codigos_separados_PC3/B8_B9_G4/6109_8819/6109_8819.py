q = int(input())

if (q < 17.5):
	t = (q + 1.5)
	print(round(t, 2))
elif (q >= 17.5) and (q < 35.):
	t = (q + 2.3)
	print(round(t, 2))
elif (q >= 35.) and (q < 50.):
	t = (q + 3.3)
	print(round(t, 2))
elif (q >= 50.):
	t = (q + 4.7)
	print(round(t, 2))