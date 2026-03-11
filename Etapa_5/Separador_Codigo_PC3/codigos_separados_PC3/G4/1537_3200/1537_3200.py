from math import *
x= float(input())
k= int(input())
soma=1.0
cont=1
exp=1

while(cont<k):
	den= (factorial(exp))
	calc= (x**exp)/den
	soma= soma + calc
	exp= exp+1
	cont= cont+1
print(round(soma,9))
	