# D.S.L.

from numpy import *

v = array(eval(input("Digite:")))

A = min(v)
B = max(v)

C = 0.75 * A + 0.25 * B
D = 0.25 * A + 0.75 * B

x1 = 0
for i in v:
	if A<=i<C:
		x1 = x1 + 1

x2 = 0
for i in v:
	if C<=i<D:
		x2 = x2 + 1
x = array([x1,x2])
print(x)


