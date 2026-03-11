from numpy import*

n=array(eval(input()))
v= zeros(size(n),dtype= int)

i=0

for i in range(size(n)):
	if n[i]%3 == 0:
		cont= cont+1
		i= i + 1
		
vetor=zeros(cont,dtype=int)
k=0
for i in range(size(n)):

   if n[j]%3 == 0:
	   v[k]= j
	   k= k +1
print(cont)
print(vetor)
