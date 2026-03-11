from math import *
n = int(input("n de termos:"))
num = 1
den = 1
i = 1
var = 0
while(i<=n):
	if(i==1):
		var = var + (sqrt(num)/(6+den))
	elif(i % 2 == 1):
		  var = var + (sqrt(num)/(6+den))
	else:
		  var = var - (sqrt(num)/(6+den))
	i = i + 1
	num  = num + 1
	den = den + 2
print(round(var,10))