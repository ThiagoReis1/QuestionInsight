from numpy import *
v = array(eval(input("valores do vetor:")))
t = size(v)
i = 0
a = (sum(v** (1/2)))
M = (a / t) ** 2
print(round(M, 2))
