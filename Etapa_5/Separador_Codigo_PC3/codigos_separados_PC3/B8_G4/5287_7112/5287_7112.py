a = input().upper()

c = 0
d = 0

while( a!= "S"):
	
	if(a == "CARA"):
		c = c+1
		
	elif( a == "COROA"):
		d = d+1
	a = input().upper()
	
t = c+d
y = 100* c /t
print(t) 
print(round(y, 2))
