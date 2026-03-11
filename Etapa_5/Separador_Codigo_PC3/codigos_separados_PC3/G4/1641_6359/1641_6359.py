from numpy import*
l=array(eval(input("Lista: ")))
cont=0

for c in range(size(l)):
	if l[c]%3==0:
		cont=cont+1
		
v=zeros(cont,dtype=int)
d=0

for x in range(size(l)):
	if l[x]%3==0:
		v[d]=x
		d=d+1
		
print(cont)
print(v)