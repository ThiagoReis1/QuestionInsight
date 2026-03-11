from math import *
n = int(input("n de termos:"))
num = 1
den = 3
i = 1
var = 0
while(i<=n):
	if(i==1):
		  var = -1/9
	elif(i % 2 == 0):
		  var = var + (sqrt(num)/(6+den))
	else:
		  var = var - (sqrt(num)/(6+den))
	i = i + 1
	num  = num + 1
	den = den + 2
print(round(var,5))