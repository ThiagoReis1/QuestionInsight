from numpy import*

v=array(eval(input("digite o vetor v: ")))
A=min(v)
B=max(v)

C=0.6*A+0.4*B
D=0.3*A + 0.7*B

x1=0
x2=0
for i in range(0,size(v)):
	if(C <= v[i]and v[i] < D):
		x1= x1 + 1
	elif(D <= v[i]and v[i] < B):
		x2=x2+1
x=array([x1,x2])
print(x)