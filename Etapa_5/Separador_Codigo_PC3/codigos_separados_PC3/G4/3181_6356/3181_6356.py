from numpy import *
l=array(eval(input("Informe vetor: ")))
new=zeros(37,dtype=int)
for i in range(size(l)):
	n=l[i]
	if l[i]==n:
		new[n]+=1
print(new)