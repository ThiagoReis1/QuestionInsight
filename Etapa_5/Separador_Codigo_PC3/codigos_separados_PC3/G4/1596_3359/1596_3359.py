from numpy import*
from numpy.linalg import *

a = array(eval(input("digite as notas: ")))

tot = sum(a)
t = tot - min(a)

m = t / (size(a) - 1)

print(round(m,2))