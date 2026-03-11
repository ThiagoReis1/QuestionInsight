from numpy import *
from numpy.linalg import *

v = array(eval(input("notas = ")))

n = round((sum(v) - min(v)) / (size(v) - 1), 2)

print(n)