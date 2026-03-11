qi = int(input())
qpd = int(input())
r = int(input())

x = 0

while(qi > 0):
	qi = (qi - qpd) + r
	
	x = x+1
	
print(int(x))