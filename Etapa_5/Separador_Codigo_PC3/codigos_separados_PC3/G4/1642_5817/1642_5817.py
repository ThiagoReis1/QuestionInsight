from numpy import*
v=array(eval(input("Vetor: ")))
cont=0

for i in range(size(v)):
	if v[i]%5==0:
		cont+=1
		
new=zeros(cont,dtype=int)
k=0
for j in range(size(v)):
	if v[j]%5==0:
		new[k]=j
		k+=1
		
print(cont)
print(new)