from numpy import*

vet= array(eval(input('vet:')))

v0= zeros(size(vet), dtype=int)
j=0
apv=0
s=0
for i in range(size(vet)):
	if(vet[i]>= 70):
		apv=apv+1
		v0[j]= i
		j=j+1
		
s0= zeros(j, dtype=int)

for s in range(size(v0)):
	if(v0[s]!=0):
		s0[s]= v0[s]
	
print(apv)
print(s0)
		