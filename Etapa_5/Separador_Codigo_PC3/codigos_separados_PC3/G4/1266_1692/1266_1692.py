# Wagner William Amorim - 21552149
# Av 6 
# Questão 02
# 25/08/2016

from numpy import *
from math import *

p = float(input("Digite p: "))
x = array(eval(input("Digite o vetor x: ")))
y = array(eval(input("Digite o vetor y: ")))

t = (p) / (p - 1)
n = 0
xy = ((2 * x) - y)

for i in xy:
	n = n + (abs(i)) ** t
v = n ** (1 / t)
print(round(v, 4))