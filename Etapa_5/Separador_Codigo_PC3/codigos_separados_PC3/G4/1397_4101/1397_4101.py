a = int(input())

v = 5*a
ve = (a//10000)*50000 + (a%10000)*4

if (a < 10000):
	print(round(v, 2))
else: 
	print(round(ve, 2))