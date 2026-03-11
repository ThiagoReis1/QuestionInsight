n = float (input(""))

if(n >= 3000.0 and n < 3400.0):
	x = n * 0.8
	
elif(n >= 3400 and n < 3900.0):
	x = n * 1.3
	
elif(n >= 3900.0 and n < 4100.0):
	x = n * 2.1
	
else:
	x = n *3.0

	
print(round(x, 1))