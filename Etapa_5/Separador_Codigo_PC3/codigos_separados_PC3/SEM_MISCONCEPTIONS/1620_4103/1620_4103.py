from numpy import *
from numpy.linalg import *

tempo = array(eval(input("Tempo do banho: ")))
percentual = array(eval(input("Valor da porcentagem: ")))

x = tempo*5
p = dot(x, percentual)
y = p/100
t = sum(y)

print(round(t, 2))
