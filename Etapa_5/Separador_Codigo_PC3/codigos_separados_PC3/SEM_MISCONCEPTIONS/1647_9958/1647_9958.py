from numpy import *

freq = array(eval(input("medias")))
aprovados = 0

for x in freq:
	if x>=70:
		aprovados+=1

vaprov=zeros(aprovados,dtype=int)
j=0
for i in range(size(freq)):
	if freq[i]>=70:
		vaprov[j]=i
		j+=1

print(aprovados)
print(vaprov)