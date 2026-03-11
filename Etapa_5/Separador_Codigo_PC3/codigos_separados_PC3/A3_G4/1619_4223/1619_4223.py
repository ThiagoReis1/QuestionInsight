from numpy import*
from math import*

temp=array(eval(input("tempo em min: ")))
modos=array(eval(input("")))
t=0.005

c1=(temp*t)

s=sum(c1)
print(round(s, 2))