from numpy import*
vet=(array(eval(input("vetor:"))))
a=1
x=0
for i in range(size(vet)):
	a=a*vet[i]
x=a**(1/size(vet))
print(round(x,2))