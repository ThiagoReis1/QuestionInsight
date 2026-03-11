area = float(input("area a ser fertilizada: "))


c1 = (area * 5)

c2 = ((10000 * 5) + (4 * (area - 10000)))

if(area > 10000):
	m = c2

else:
	m = c1

	
print(round(m, 2))