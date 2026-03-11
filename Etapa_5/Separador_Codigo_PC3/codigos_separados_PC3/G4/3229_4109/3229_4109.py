from numpy import*
from numpy.linalg import*

x = array(eval(input('Moedas: ')))

y = x.T

M = array([[1, 1],
			 [0.25, 0.5]])

moedas = dot(inv(M), y)

print(moedas)