# Mayara Soares
# 25 - 08 - 2016
# Av. 06  Ex. 01

from numpy import *

v = array(eval(input("Digite um vetor: ")))
x = array(zeros(2, dtype = int))

A = min(v)
B = max(v)

C = 0.7 * A + 0.3 * B
D = 0.4 * A + 0.6 * B


for x1 in x:
	if x1 >= A and x1 < C:
		print(x1)

for x2 in x:
	if x2 >= C and x2 < D:
		print(x2)
		
print(x)