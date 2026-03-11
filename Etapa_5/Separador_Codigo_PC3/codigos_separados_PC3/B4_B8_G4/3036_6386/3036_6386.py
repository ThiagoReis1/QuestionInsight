x = float(input("valor de x: "))

if x <= -1 or x >= 1:
	fx = x
elif (x > -1 and x < 0):
	fx = 1
elif (x > 0 and x < 1):
	fx = 1
elif x == 0:
	fx = 2
	
print(round(fx,2))
