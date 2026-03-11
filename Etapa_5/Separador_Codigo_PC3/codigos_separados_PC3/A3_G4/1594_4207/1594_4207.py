from numpy import*

da= array(eval(input("Insira os danos: ")))

i=0
p=1
ac=0
x=size(da)

while(i<x):
	if(da[i]==0):
		dano=da[0]*p
		p=p+1
		
	dano=da[i]*(p+1)
i=i+1
print(dano)


