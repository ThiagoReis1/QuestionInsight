from numpy import*
v=array(eval(input("")))

p=200
pot=0
i=0

while i<size(v):
	if v[i]==1:
		p=p*4
	if v[i]==2:
		p=p*2
	if v[i]==3:
		p=p
	if v[i]==4:
		p=p/2
	pot=p
	i=i+1
print(round(pot, 2))
	