from numpy import*

v=array(eval(input("Mensagem: ")))
s=size(v)
z=zeros(s, dtype=int)

for i in range(size(v)):
	if v[i]>0:
		z[i]=v[i]-1
	elif v[i]==0:
		z[i]=9
print(z)