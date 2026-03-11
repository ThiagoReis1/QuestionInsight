from numpy import*
from numpy import*

p = float(input("Digite um numero: "))
x = array(eval(input("vetor1: ")))
y = array(eval(input("vetor1: ")))
n = 0 
t = ((p) / (p + 1))
xy = (x + y)
for i in xy:
	n = n + (abs(i)) ** t
v = n ** (1 / t)
print(round(v, 3))