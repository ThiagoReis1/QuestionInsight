from numpy import*
p=int(input())
t=p/(p+1)
x=array(eval(input()))
y=array(eval(input()))
z=array(zeros(size(x)))
w=array(zeros(size(x)))
for i in range(size(z)):
	z[i]=x[i]+y[i]
	z[i]=abs(z[i]**t)
q1=(sum(z))**1/t
for i in range(size(w)):
	w[i]=x[i]-y[i]
	w[i]=abs(w[i])**t
q2=(sum(w))**1/t
print(round(q1-q2, 7))	