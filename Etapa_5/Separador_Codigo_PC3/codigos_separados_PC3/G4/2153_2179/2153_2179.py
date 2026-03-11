from numpy import *
from math import *

x = array(eval(input("x: ")))
y = array(eval(input("y: ")))

soma = 0

for j in range(size(x)):
	soma = soma + (x[j] - y[j])**2

d = sqrt(soma)
	
print(round(d, 4))