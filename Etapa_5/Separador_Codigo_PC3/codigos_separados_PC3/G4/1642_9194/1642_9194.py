from numpy import*
v= array(eval(input("inserir vetor:")))
ac=0

for i in range(size(v)):
	if v[i]%5==0:
		ac+=1
print(ac)

b=0
n= zeros(ac,dtype = int)

for i in range(size(v)):
	if v[i]%5==0:
		n[b]=i
		b= b+1
print(n)