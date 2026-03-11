c = float(input("peso do tripulante: "))

if (c >= 3000.0 and c < 3400.0):
	c1 = (c * 0.8)

elif (c >= 3400.0 and c <3900.0):
	c1 = (c * 1.3)
	
elif (c >= 3900.0 and c <4100.0):
	c1 = (c * 2.1)
	
else:
	c1 = (c *3.0)
	
print(c1)