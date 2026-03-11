from numpy import *

v = array(eval(input("digite: ")))
sizevetor = size[-1]

n = sum(v)

m = ((v[0]**-1 + v[1]**-1 + v[2]**-1+ v[ - 1]**-1)/n)**-1

print(round(m, 2))
