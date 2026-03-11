from numpy import*
from numpy.linalg import*

m = array(eval(input()))
M = m.T

s = array([[1,1],
			  [0.25, 0.5]])

moedas = dot(inv(s), M)

print(moedas)