from numpy import*
from math import*
p=(float(input("digite o numero: ")))
v1= array(eval(input("Digite o vetor: ")))
v2= array(eval(input("Digite o vetor: ")))
t=(p/p-1)
soma=0
for i in range(size(v1)):
	soma= soma+(abs(v1[i]+v2[i]))**t
	raiz= soma**1/t
print(round(raiz,5))