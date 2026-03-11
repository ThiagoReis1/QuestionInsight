from numpy import *

nt = array(eval(input("Notas: ")))
p = array([4, 3])

n = nt * p

media = sum(n) / sum(p)
print(round(media,2))