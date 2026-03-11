from numpy import*
x=array(eval(input("numeros.")))
p=-1
n=zeros(size(x),dtype=int)
for i in range(size(x)):
	if(x[i]!=0):
		p=p+1
		n[p]=x[i]
print(n)