from numpy import*
l=array(eval(input("Lista: ")))
q=size(l)
v=zeros(3,dtype=int)
s=zeros(10,dtype=int)

for i in range(size(l)):
	if l[i]%3==0: