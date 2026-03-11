from numpy import *

p = array([3,2,4,1,3])

v = array(eval(input("Notas: ")))

tot = (v[0]*p[0] + v[1]*p[1] + v[2]*p[2] + v[3]*p[3] + v[4]*p[4])/13

print(round(tot,2))