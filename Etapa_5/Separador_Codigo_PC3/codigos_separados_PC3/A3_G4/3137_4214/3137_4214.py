from numpy import *
vn=array(eval(input("Valores:")))

a=exp(vn)
b=sum(a)
c=size(vn)
m= log(sum(a)/exp(c))

print(round(m,2))