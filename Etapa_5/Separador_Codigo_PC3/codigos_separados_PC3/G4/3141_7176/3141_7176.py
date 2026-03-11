from numpy import*
vet=(array(eval(input("vetor:"))))
a=0
for i in range(size(vet)):
	a=a+vet[i]**(1/6)
r=(a/size(vet))**6
print(round(r,2))