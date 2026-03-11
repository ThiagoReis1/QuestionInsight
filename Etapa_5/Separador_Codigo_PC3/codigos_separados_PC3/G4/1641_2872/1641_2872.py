from numpy import*
v = (array(eval(input(": "))))
t=0
for i in v:
	if ((i%3)==0):
		t = t+1
print(t)
q = zeros(t,dtype=int)
t = 0
m = 0
for i in v:
	if ((i%3)==0):
		q[t]= m
		t = t+1
	m= m+1
print(q)
	