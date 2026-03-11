from numpy import *
from numpy.linalg import *

tempo = array(eval(input("Digite o tempo de banho: ")))
percentual = array(eval(input("Digite o percentual: ")))

P = (percentual/100) * 5
P = P.T

total = dot(P, tempo)

print(total)