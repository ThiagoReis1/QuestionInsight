from numpy import*
from numpy.linalg import *
pagar=array(eval(input()))

pagar=pagar.T
sistema=array([[1,1],
				  [0.25,0.5]])
print(dot(inv(sistema),pagar))