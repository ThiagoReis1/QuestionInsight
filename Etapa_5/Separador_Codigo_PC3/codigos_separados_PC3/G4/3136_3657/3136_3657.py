from numpy import*
from math import*
M=array(eval(input('De o vetor de valores reais: ')))
n=size(M)
i=0
soma=0
while(i<n):
	soma=soma+log(M[i]+1)
	i=i+1
media=exp(soma/n)-1
print(round(media,2))
	