from numpy import *

v = array(eval(input("Notas: ")))

z = arange(size(v))+1

v = v*z
m = sum(v)/sum(z)

print(round(m, 2))