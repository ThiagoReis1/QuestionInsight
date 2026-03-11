from numpy import *

vetor = array(eval(input()))

cont=0

for i in range(size(vetor)):
	if vetor[i]%3==0:
		cont=cont+1
final=zeros(cont, dtype=int)
j=0
for i in range(size(vetor)):
	if vetor[i]%3==0:
		final[j]=i
		j=j+1
print(cont)
print(final)