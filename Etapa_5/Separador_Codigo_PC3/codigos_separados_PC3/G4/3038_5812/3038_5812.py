import math

x = float(input())

if (x<=-1)or(x>=1):
	y = math.sqrt(abs(x))
elif (x == 0):
	y = 0
else:
	y = abs(x)
	
print(round(y,2))