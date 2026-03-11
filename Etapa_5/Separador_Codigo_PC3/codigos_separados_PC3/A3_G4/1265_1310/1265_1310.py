from numpy import *
p=float(input("p: "))
x=array(eval(input("x: ")))
y=array(eval(input("y: ")))
h=0
n=0
j=0
t=((p)/(p-1))
for i in x:
	n=n+(abs(2*i+y[j]*3)**t)
	j=j+1
v=n**(1/t)
print(round(v,3))