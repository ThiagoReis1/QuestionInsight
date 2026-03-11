from numpy import*

vet= array(eval(input("quantidade: ")))

p=0
j=0
for i in range(size(vet)):
	if vet[i]%2==0:
		p+=1
resul=zeros(p,dtype=int)

for i in range(size(vet)):
	if vet[i]%2==0:
		resul[j]=i
		j=j+1
			
print (p)
print(resul)
		

