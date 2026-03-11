from numpy import *
from numpy.linalg import *
pagar = array(eval(input()))
pagar = pagar.T
sis = array([[1,1],[0.25,0.5]])
m = dot(inv(sis),pagar)
print(m)