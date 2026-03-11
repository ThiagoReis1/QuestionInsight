from numpy import *
from numpy.linalg import *
a=array(eval(input("Moedas:")))
a=a.T
sistema=array([[1,1],[0.25,0.5]])
result=dot(inv(sistema),a)
print(result)