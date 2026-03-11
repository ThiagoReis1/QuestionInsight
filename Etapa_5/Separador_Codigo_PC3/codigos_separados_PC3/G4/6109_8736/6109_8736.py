combo = float(input("Combustivel : "))

if (combo < 17.5):
	v = combo + 1.5
	print(v)
elif (17.5 < combo < 35):
	v2 = combo + 2.3
	print(v2)
elif (35 < combo < 50):
	v3 = combo + 3.3
	print(v3)
else :
	v4 = combo + 4.7
	print(v4)