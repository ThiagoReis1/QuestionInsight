from numpy import *
p=float(input(""))
x=array(eval(input("")))
y=array(eval(input("")))
h=0
n=0
j=0
t=((p)/(p-1))
xy=(2*x-y)
for i in xy:
	n=n+(abs(i))**t
v=n**(1/t)
print(round(v,4))