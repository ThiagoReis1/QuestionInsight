from numpy import *
from numpy.linalg import *
m = array(eval(input("matriz m: ")))
l = m.shape[0]
c = m.shape[1]
v = zeros(l, dtype=float)
a = 