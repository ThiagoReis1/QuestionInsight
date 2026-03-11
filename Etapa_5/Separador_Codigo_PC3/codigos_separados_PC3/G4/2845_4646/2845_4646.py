from numpy import*
v = array(eval(input("vetor")))
s =zeros(size(v),dtype=int)
for i in range(size(v)):
	if(v[i]==9):
		v[i]=0
	else:
		s[i]=v[i]+1
print(s)
