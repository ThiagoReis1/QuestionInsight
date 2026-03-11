from numpy import*
v = array(eval(input("vetor:")))
i=0
r=0
s=[]
while i<size(v):
	if (v[i]>=2000)and(v[i]>0):
		r=r+1
		s.append(i)
	i=i+1
print(r)
print(array(s))