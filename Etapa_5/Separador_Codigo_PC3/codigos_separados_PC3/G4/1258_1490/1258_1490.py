from numpy import*
p=float(input(""))
x=array(eval(input("")))
y=array(eval(input("")))
t=p/(p+1)
v=0
for i in range(size(x)):
	v = ((abs(x[i]+y[i]))**t)+v
v = (v)**(1/t)
print(round(v,3))