from numpy import*
v = array(eval(input()))
v1 = array(zeros(2,dtype = int))
A=min(v)
B=max(v)
C = 0.6*A + 0.4*B
D = 0.3 * A + 0.7*B
for i in range(size(v)):
	if v[i] >=C  and v[i]<D:
		v1[0]=v1[0]+1
	elif v[i]>=D and v[i]<B:
		v1[1]=v1[1]+1
print(v1)		