from numpy import *

p = [3, 2, 4, 1, 3]
n = array(eval(input()))
nota1 = (p[0] * n[0])
nota2 = (p[1] * n[1])
nota3 = (p[2] * n[2]) 
nota4 = (p[3] * n[3])
nota5 = (p[4] * n[4])

total = (nota1 + nota2 + nota3 + nota4 + nota5) / sum(p)
print(round(total,2))