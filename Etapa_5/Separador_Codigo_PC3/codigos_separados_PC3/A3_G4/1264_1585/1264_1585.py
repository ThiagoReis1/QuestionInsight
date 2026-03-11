from numpy import*
p = float(input("p:"))
x = array(eval(input("x:")))
y = array(eval(input("y:")))
h=0
n=0
j=0
t= ((p)/(p + 1))
xy = (x - 2*y)
for i in xy:
	n = n+(abs(i)**t)
v=n**(1/t)
print(round(v,8))