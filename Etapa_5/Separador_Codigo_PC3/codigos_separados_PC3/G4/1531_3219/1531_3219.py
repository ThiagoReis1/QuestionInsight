from math import*
x= eval(input())
k= int(input())
soma= 0
l= 1
v= 0
cont=1

while (v != k ):
	soma= soma + ((cont)**(v+1)) * ((x**1)/(factorial(l)))
	cont= cont*-1
	l= l + 2
	v= v+ 1
print(round(soma,10 ))