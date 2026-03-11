#aprovados
from numpy import*

fq=array(eval(input("Digite o vetor frequencia:")))
ap=0
j=0

for i in fq:
	if (i>=70):
		ap= ap+1
ind= zeros(ap, dtype=int)

for i in range(size(fq)):
	if (fq[i]>=70):
		ind[j]= i
		j= j+1
print(ap)
print(ind)
		