from numpy import *
p = float (input(""))
x = eval(input(""))
y = eval(input(""))
q= p/(p+1)
v=zeros(size(x), dtype=float)
for i in range(size(x)):
	v[i]=x[i]-2*y[i]
s=0
for j in v:
	s = abs(j)**q
print(round(s**(1/q),8))