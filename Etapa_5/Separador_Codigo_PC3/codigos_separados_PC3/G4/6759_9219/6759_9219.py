d = int(input("Distancia em KM:  "))
if d < 10:
	t = 50 + 5.50
elif d == 10:
	t = 50 + 7.75
else:
	t = 50 + 10.00

print(round(t, 2))