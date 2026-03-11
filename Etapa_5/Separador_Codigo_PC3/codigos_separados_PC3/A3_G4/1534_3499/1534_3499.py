x = float(input())
k = int(input())
c = x
acm = 0
d = 1
while(acm < x):
	x = x + ((1)**(d + 1)**(x*k))/x
	acm = acm + x
	print(round(acm, 7))
	
