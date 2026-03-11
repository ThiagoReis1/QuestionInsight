from numpy import *

p=float(input("Digite o numero real: "))
x=eval(input("Qual o vetor x: "))
y=eval(input("Qual o vetor y: "))

q=p/(p+1)

v=zeros(size(x),dtype=float)
for i in range(size(x)):
	v[i]=x[i]-2*y[i]

soma=0
for j in v:
	soma+=abs(j)**q
	
print(round(soma**(1/q),8))

