from numpy import*
from numpy.linalg import *

tempo = array(eval(input()))
consumo = array(eval(input()))

x = (consumo / 100) * 5
x = x.T

y = dot(x,tempo)

print(y)