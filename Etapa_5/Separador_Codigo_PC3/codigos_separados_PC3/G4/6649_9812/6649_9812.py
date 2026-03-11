from numpy import *

v = array(eval(input("vetor de notas: ")))

v2 = [3,2,4,1,3]

vp = v * v2
vn = sum(vp)
vm = sum(v2)

print(round(vn/vm,2))