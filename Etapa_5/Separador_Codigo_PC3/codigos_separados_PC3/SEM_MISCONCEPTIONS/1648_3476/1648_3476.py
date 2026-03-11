from numpy import*

v=array(eval(input("Digite v: ")))
aprov=0
reprov=0
for cont in v:
	if(cont<70):
		reprov=reprov+1
	else:
		aprov=aprov+1
v2=zeros(reprov,dtype=int)
i=0
for cont in range(0,size(v)):
	if(v[cont]<70):
		v2[i]=cont
		i=i+1
print(reprov)
print(v2)