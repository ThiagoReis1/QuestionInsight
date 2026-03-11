from math import * 
n = int(input("n:"))
x = 3
h = 5
f = 1
i = 0
var = 
while( i == n):
	if( x % 2 != 0):
		var = sqrt(x)/ (h + f)
	else:
		var = - (sqrt(x)/(h + f))
	x = x + 1
	f = f + 1
	i = i + 2
print(round(var,10))
