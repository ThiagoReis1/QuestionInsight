from numpy import*
v = array(eval(input()))
a= min(v)
b= max(v)
c=0.65*a + 0.35*b
d=0.45*a + 0.55*b
x = zeros(2,dtype = int)
i = 0
while(i < size(v)):
	if(v[i]>=a)and(v[i]<c):
		x[0]=x[0]+1
	elif(v[i]>=c)and(v[i]<d):
		x[1]=x[1]+1
	i = i +1
print(x)

abs(x[i])**t