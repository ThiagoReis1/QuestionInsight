from numpy import*
v=array(eval(input()))
A=min(v)
B=max(v)
C = 0.6 * A + 0.4 * B
D = 0.3 * A + 0.7 * B
t=0
j=-1
for i in range(size(v)):
	if v[i]>=A and v[i]<C:
		t+=1
	elif v[i]>=D and v[i]:
		j+=1
x=array(zeros(2,dtype=int))
x[0]=t
x[1]=j
print(x)