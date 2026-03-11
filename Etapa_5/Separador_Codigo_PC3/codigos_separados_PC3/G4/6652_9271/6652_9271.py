from numpy import *
v = array(eval(input("Digite as notas: ")))
p = [2,2,6,1]

mp = sum(v * p) / sum(p)
print(round(mp,2))