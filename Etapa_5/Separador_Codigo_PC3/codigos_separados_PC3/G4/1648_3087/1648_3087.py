from numpy import*

v= array(eval(input("aulas frequentadas: ")))
rep=0
n=size(v)

for i in range(n):
	if(v[i]<70):
		rep=rep+1
		
saida=zeros(rep,dtype=int)
j=0
for i in range(n):
	if(v[i]<70):
		saida[j]=i
		j=j+1
		
print(rep)
print(saida)