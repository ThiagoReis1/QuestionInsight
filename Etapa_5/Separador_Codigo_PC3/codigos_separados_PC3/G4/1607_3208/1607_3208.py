from numpy import*
v=array(eval(input()))

d1=v[1]-v[0]
s=d1*3
d2=v[2]-v[1]
a=d2*3
d3=v[3]-v[2]
b=d3*3
d4=v[4]-v[3]
c=d4*3
j=s+a+ s+b +s+c+a+b+a+c


print(j)
