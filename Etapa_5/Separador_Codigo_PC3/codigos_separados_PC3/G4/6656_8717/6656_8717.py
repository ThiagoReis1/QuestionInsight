from numpy import *
v = array([3,4,2,1,4,5])

n = array(eval(input("Notas: ")))

s = v * n

x = sum(s)/19
print(round(x, 2))
