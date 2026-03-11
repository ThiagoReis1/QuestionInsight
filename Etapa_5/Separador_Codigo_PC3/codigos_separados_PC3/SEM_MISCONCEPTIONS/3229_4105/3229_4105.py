from numpy import*
from numpy.linalg import*
A=array([[1,1],[0.25,0.5]])
b=array(eval(input("")))
b=b.T

moedas=dot(inv(A),b)
print(moedas)