from math import *
x=eval(input())
k=int(input())
total=0
y=2*k
while(k>0):
	total=1-(x**(y)/factorial(y))+total
print(round(total, 10))	