from numpy import*
v=array(eval(input("frequencia: ")))
p=70


r=0#quantidade
novo=zeros(r,dtype=int)
for i in range(size(v)):
	if(v[i]<p):
		r=r+1

print(r)
novo=zeros(r,dtype=int)
j=0
for i in range(size(novo)):
	novo[i]=i
print(novo)
