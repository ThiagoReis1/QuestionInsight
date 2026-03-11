from numpy import *
v=array(eval(input('Jogadas:')))
t=0
p=200
while t<size(v):
	if v[t]==1:
		p=p*4
		t=t+1
	elif v[t]==2:
		p=p*2
		t=t+1
	elif v[t]==3:
		t=t+1
	elif v[t]==4:
		p=p/2
		t=t+1
print(round(p,2))
x=v[i+1]-v[i]
if x <0:
	b=b-x