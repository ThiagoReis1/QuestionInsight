from numpy import*

f=array(eval(input("Digite o percentual de faltas dos alunos: ")))

aprov=0

for i in range(size(f)):
	if(f[i]>=70):
		aprov=aprov+1
		
z=zeros(aprov,dtype=int)

j=0
for p in range(size(f)):
	if(f[p]>=70):
		f[p]=p
		z[j]=z[j]+f[p]
		j=j+1
		

print(aprov)
print(z)




