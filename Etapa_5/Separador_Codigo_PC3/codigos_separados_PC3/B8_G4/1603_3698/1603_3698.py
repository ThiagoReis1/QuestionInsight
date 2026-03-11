from numpy import * 
v = array(eval(input("Digite: ")))
t = 0
p = 0
while t<size(v):
	if v[t]==1:
		p=p+80
		t=t+1
	elif v[t]==2:
		p=p+40
		t=t+1
	elif v[t]==3:
		p=p+20
		t=t+1
	elif v[t]>=4:
		t=t+1
print(round(p,2))