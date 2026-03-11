from numpy import *
vp = array([5,1])
v = array(eval(input("v: ")))
#numerador
n = vp * v
num = sum(n)
#denominador
d = sum(vp)
total = num/d
print(round(total,2))