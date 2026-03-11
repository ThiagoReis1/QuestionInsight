a = int(input("area "))
c1 = a * 5
c2 = (10000*5) + ((a-10000)*4)

if (a <= 10000):
	print(round(c1,2))
else: 
	print(round(c2,2))