from numpy import *

p= eval(input("digite um numero maior que 1:"))

x=array(eval(input("digite um vetor:")))
y= array (eval(input("digite um vetor:")))

k=0
i=0
for i in range(size(x)):
	x[i]=x[i]-y[k]
	i=i+1
	k=k+1
print(x)

q= p/(p+1)

soma=0

for t in x:
	soma = soma + (abs(t))**(q)
norma= (soma)**(1/q)
print(round(norma,4))