from numpy import*
from math import*
v1 = array(eval(input("")))
v2 = array(eval(input("")))

#v = (v1[0]*v2[0]+ v1[1]*v2[1] + v1[2]*v2[2] + v1[3]*v2[3])/60
#vv = (v1[0]*v2[0]+ v1[1]*v2[1] + v1[2]*v2[2] + v1[3]*v2[3])/100
v = v1 * 5*v2/100
t = sum([v])
#vvv = print(round(v+vv,2))
print(round(t,2))
