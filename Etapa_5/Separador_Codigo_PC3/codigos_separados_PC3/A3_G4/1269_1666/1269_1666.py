from numpy import *
from numpy import *
p = float(input("Digite p :"))
x = array(eval(input("Digite o vetor x :")))
y = array(eval(input("Digite o vetor y :")))
h = 0
n = 0
j = 0
t = ((p) / (p + 1))
for i in range(0,size(x)):
	n = n + (abs(x[i]+y[i])) ** t
n = n ** ( 1 / t)
for i in range(0,size(y)):
	h = h + (abs(x[i]-y[i])) ** t
h = h ** ( 1 / t)
j = n - h
print(round(j,7))