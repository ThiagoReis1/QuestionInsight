from numpy import *
a = eval(input())
x = 0
cont = 0
recorde = 8.95
while(x < size(a)):
	if(a[x]<recorde):
		cont = cont + 1
	x = x + 1
print(recorde)
print(cont)
