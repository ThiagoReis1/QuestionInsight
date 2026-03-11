from numpy import *
from numpy import *
p = float(input("Digite p: "))
x = array(eval(input("Digite o vetor x: ")))
y = array(eval(input("Digite o vetor y: ")))
h = 0
n = 0
j = 0
t = ((p) / (p-1))
xy=  (x + y)
for i in xy:
	n = n + (abs(i)) ** t 
v = n ** (1 / t)
print(round(v,5))