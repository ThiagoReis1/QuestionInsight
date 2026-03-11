from math import*

x = float(input())
k = int(input())

i= 0
cx = 0

while(k > i):
	
	cx = cx + (x**(2*i))/factorial(2*i)
	i = i + 1 
	
print(round(cx,8))