from numpy import*
from numpy.linalg import*

t = array(eval(input('Tempo dos banhos: ')))
p = array(eval(input('Abertura da torneira: ')))

x = (p/100)*5
y = x.T


a = dot(y, t)
print(a)

