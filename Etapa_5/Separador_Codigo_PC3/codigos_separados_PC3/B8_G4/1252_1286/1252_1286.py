from numpy import *
v = array(eval(input()))
v2 = array(zeros(2,dtype=int))
a = min(v)
b = max(v)
c = (0.6*a) + (0.4*b)
d = (0.3*a) + (0.7*b)
for i in v:
 if(i>=a and i<c):
  v2[0] = v2[0]+1
 elif(i>=c and i<d):
  v2[1] = v2[1]+1

print(v2)