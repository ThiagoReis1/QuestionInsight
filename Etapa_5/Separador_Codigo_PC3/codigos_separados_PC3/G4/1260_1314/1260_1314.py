from numpy import*
p=float(input("digite um numero maior que 1:"))
x=array(eval(input("Vetor x:")))
y=array(eval(input("Vetor y:")))
t=p/(p+1)
v=x-y
isso=0
k=0
while k<size(v):
	isso=((abs(v[k]))**t)+isso
	k=k+1
norma=(isso)**(1/t)
print(round(norma,4))