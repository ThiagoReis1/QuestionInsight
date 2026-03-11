#Suenne Renata Lima Fernandes- 21602342

from numpy import*
v = array(eval(input("")))
r = 74.08
print(r)
i = 0
cont = 0
while(i < size(v)):
	if( v[i] > r):
		cont = cont + 1
	i = i + 1
print(cont)	