#nota menor que 5
from numpy import *
v = array(eval(input('notas:')))
a=0
t=0
while t<size(v):
	if v[t]<5:
		a+=1
	t+=1
t=0
y=0
x=zeros(a,dtype=int)
print(a)
while t<size(v):
	if v[t]<5:
		x[y]=t
		y+=1
	t+=1
print(x)