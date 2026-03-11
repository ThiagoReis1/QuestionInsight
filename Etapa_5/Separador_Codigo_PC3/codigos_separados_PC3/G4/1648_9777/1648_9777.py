from numpy import*
saque= array(eval(input()))
cont=0
for i in range(size(saque)):
	if saque[i]<70:
		cont+=1
ind= zeros(cont, dtype=int)
print(cont)
j=0
for  i in range(size(saque)):
	if saque[i]<70:
		ind[j]=i
		j+=1
print(ind)