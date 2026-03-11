from numpy import*

vtr1=array(eval(input("vetor:")))
x=array(zeros(2,dtype=int))
a=min(vtr1)
b=max(vtr1)
c=0.85*a+0.15*b
d=0.4*a+0.6*b
j=0
i=0  #cont
x1=0 #ac
x2=0 #ac

for i in range(0,size(vtr1)):
	if vtr1[i]>=a and vtr1[i]<c:
			x1=x1+1
			x[j]=x1
	if vtr1[i]>=d and vtr1[i]<b:
			x2=x2+1
			x[j+1]=x2
			
			
i=i+1

print(x)