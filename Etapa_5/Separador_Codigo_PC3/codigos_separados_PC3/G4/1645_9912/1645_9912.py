from numpy import*
v=array(eval(input("valores: ")))
cont=0

for i in v:
	if i>=2000:
		cont+=1
print(cont)

x=0
s=zeros(cont,dtype=int)
for i in range(size(v)):
	if v[i]>=2000:
		s[x]=i
		x+=1
print(s)
		

	