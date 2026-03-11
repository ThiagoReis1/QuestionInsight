from numpy import*

n = array(eval(input("")))
v = array([5,4,3,2])
v0 = dot(n,v)

print(round(v0/sum(v),2))