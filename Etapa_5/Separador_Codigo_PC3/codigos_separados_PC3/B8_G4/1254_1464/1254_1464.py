from numpy import*
v=array(eval(input("v:")))

for i in v:
	if(i==min(v)):
		A=i
	elif(i==max(v)):
		B=i
C=0.6*A+0.4*B
D=0.3*A+0.7*B
x1=0
x2=0
j=0
for j in v:
	if(j>=C and j<D):
		x1=x1+1
	elif(j>=D and j<B):
		x2=x2+1
x=array([x1,x2])
print(x)
	