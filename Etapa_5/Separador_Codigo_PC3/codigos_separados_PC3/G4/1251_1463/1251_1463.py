#Ingrid do Nascimento Mendes
from numpy import *

v1 = array(eval(input()))
v2 = array(zeros(2, dtype = int))
a = min(v1)
b = max(v1)
c = 0.7 * a + 0.3 * b
d = 0.4 * a + 0.6 * b

for x in v1:
	if (x>=c and x<d):
		v2[0] = v2[0] + 1
	if (x>=d and x<b):
		v2[1] = v2[1] + 1

print (v2)
#print("menor:",a)
#print("maior:",b)