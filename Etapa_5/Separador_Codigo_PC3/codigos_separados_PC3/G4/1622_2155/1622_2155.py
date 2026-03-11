from numpy import *
Ve = array(eval(input("notas")))
Vs = array(eval(input("notas")))
Pr1 = Ve[0]-Vs[0]
pr2 = Ve[1]-Vs[1]
pr3 = Ve[2]-Vs[2]
pr4 = Ve[3]-Vs[3]
prf = Pr1 + pr2 + pr3 + pr4
print(prf)

