from numpy import*
v = array(eval(input(" ")))
i = 0
p = 200
while i<size(v):
	if v[i]==1 or v[i]==3 or v[i]==5:
		p = p/2
	if v[i]==2 or v[i]==4 or v[i]==6:
		p = p*3
	i = i+1
print(p)