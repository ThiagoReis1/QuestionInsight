x = float(input("Indique o valor de x :"))
if( x <= 1):
	y = 1
elif(x>1 and x<=2):
	y = 2
elif(x>2 and x<=3):
	y = x**2
else:
	y = x**3
print(round(y,2))
	