from numpy import *
v= array(eval(input()))
p= 10000
i=0
while i<size(v):
	if v[i] == 1:
		p= p *2
	if v[i] == 2:
		p=p
	if v[i] == 3:
		p= p/2
	if v[i] == 4:
		p=p/4
	i+=1
print(round(p,2))
	
	