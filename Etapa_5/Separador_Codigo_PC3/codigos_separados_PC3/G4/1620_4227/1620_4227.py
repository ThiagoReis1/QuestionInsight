from numpy import*
from math import*
t = array(eval(input("")))
p = array(eval(input("")))
c1 = (t*p)
c2 = (c1/100)
c3 = (c2*5)
a = sum(c3)
print(round(a,2))