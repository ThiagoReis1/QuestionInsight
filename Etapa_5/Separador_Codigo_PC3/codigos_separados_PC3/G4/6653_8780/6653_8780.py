from numpy import *
v1 = array([3, 5, 1])
v2 = array(eval(input("Digite as notas: ")))

vn = v1 * v2

print(round(sum(vn) / sum(v1), 2))