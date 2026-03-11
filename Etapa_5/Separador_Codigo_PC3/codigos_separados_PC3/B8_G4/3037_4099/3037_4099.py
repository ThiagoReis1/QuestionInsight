x = float(input("valor de x: "))

if(x <= -1 or x >= 1):
	f = x**2
else:
	if(-1 < x < 0 or 0 < x < 1):
		f = x
	else:
		 if(x == 0):
				f = 1
			
print(round(f, 4))			