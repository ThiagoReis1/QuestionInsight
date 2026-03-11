from numpy import*

vetor=array(eval(input( )))
acum=3

for i in vetor:
	if vetor[i]>=3:
		acum=acum
print(acum)

for i in vetor:
	if vetor[i]<0:
		acum=acum+1
print(acum)

for i in vetor:
	if vetor[i]<=0:
		acum=acum-2
print(acum)

