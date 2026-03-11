from numpy import*

v= array(eval(input('v: ')))

i=0
while i<size(v):
	if v[i]>=i+1:
		t=True
	else:
		t=False
	i=i+1
print(t)