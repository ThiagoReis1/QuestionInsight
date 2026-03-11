from numpy import*
from math import*
v = array(eval(input("Digite o vetor: ")))
res = array(zeros(2, dtype=int))
A = 0
B = 0
for x in v:
	if(x==min(v)):
		A = x
	if(x==max(v)):
		B = x
C = (0.6*A)+(0.4*B)
D = (0.3*A)+(0.7*B)
x1 = 0
x2 = 0
for x in v :
	if(x>=A and x<C):
		x1 = x1 + 1
	if(x>=C and x<D):
		x2 = x2 + 1
res[0] = x1
res[1] = x2
print(res)
