from numpy import*

p=float(input("Informe o valor: "))
x=eval(input("Informe o vetor: "))
y=eval(input("Informe o vetor: "))

q= p /(p+1)

v=zeros(size(x),dtype=float)
for i in range(size(x)):
	v[i]=x[i] + y[i]
soma=0
for j in v:
	soma+=abs(j)**q

print(round(soma**(1/q),3))