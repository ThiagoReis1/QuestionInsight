from numpy import *
from math import *

p = eval(input("Digite um número: "))
x = array(eval(input("Digite um vetor: ")))
y = array(eval(input("Digite um vetor: ")))

t = p / (p - 1)

v = 2*x + 3*y

soma = 0

for i in v:
	soma = soma + (abs(i))**t 
x1 = (soma)**(1/t)
print(round(x1,3))