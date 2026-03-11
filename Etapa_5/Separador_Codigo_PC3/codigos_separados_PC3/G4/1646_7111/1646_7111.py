from numpy import*
vet= array(eval(input("Insira os valores: ")))

s= 0
i= 0
j= 0
for t in range(size(vet)):
	if (vet[t]<=50):
		s= s + 1
v= zeros(s,dtype=int)
for i in range(size(vet)):
	if (vet[i]<=50):
		v[j]= i
		j=j+1

print(s)
print(v)
	
	
	


	
	