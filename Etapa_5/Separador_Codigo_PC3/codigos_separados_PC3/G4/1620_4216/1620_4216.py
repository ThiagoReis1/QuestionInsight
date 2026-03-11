from numpy import*
from math import*
 
a= array(eval(input("")))
b= array(eval(input("")))

c1=(a*b)
c2= (c1/100)
c3= (c2*5)

a= sum(c3)
print(round(a,2))