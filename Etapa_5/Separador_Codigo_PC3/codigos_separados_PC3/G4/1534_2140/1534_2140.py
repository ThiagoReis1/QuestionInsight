num = float (input (""))
k = int (input (""))

x = 0

t = 0

while ( x<k ):
	t = t + num**(2*x+1)/(2*x+1)
	x = x + 1
print (round (t,7))
	
	