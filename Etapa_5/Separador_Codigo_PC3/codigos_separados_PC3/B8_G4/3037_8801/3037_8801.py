x = float(input())

if (x <= -1) or (x >= 1):
	f = x**2
elif (-1 < x < 0) or (0 < x < 1):
	f = x
else:
	if x == 0:
		f = 1
		
print (round(f , 4))