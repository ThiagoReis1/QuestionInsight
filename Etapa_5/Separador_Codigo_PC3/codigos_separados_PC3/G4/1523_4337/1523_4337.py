bal = 200
qi = int(input())
c = int(input())
d = int(input())

x = 0
while(qi < bal) and (qi > 0) and (c > 0) and (d > 0):
	qi = qi + c - d
	x = x + 1
print(x)
	
