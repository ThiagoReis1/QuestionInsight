x = float(input("valor de x: "))

if( x == 0):
	t = 1
if(-1 < x and x <0 or 0 < x < 1):
	t = x
if(x<= -1 or x >= 1):
	t = x**2
print(round(t,4))