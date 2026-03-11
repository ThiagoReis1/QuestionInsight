from numpy import*
p=eval(input('p'))
x=array(eval(input('Vetor:')))
y=array(eval(input('Vetor:')))
t=p/(p+1)
v=x-2*y
isso=0
k=0
while k<size(v):
	isso=((abs(v[k]))**t)+isso
	k=k+1
norma=(isso)**(1/t)
print(round(norma,8))
	