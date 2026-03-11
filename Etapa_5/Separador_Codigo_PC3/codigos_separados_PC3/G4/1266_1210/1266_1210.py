from numpy import *
p= float(input("Informe um número real:"))
x=array(eval(input("informe o vetor 1:")))
y=array(eval(input("informe o vetor 2:")))
t=p/(p-1)
s=(2*x-y)
i=0
soma=0
while(i<size(s)):
	soma=soma+(s[i])**(1/t)
	i=i+1
soma=(abs(soma))**(1/t)
print(round(soma,4))
