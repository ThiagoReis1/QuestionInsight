from math import*
n = int(input("informe um numero inteiro: "))
num = 1
den = 1
i = 1
var = 0

while(i <= n):
	if(i == 1):
		var = 1/7
	elif(i % 2 == 0):
		var = var + (sqrt(num)/(6+den))
		den = den + 2
	else:
		var = var - (sqrt(num)/(6+den))
		den = den + 2
	i = i + 1
	num = num + 1
print(round(var,10))