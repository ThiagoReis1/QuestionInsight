from numpy import*
v = array(eval(input("digite")))
cont=zeros(2,dtype=(int))
A=min(v)
B=max(v)
C = 0.75*A + 0.25*B
D = 0.25*A + 0.75*B
for i in range(size(v)):
	if(v[i]>=A and v[i]<C):
	   cont[0]=cont[0]+1
	elif(v[i]>=D and v[i]<B):
		cont[1]=cont[1]+1
print(cont)		 