from numpy import*
v=array(eval(input('Digite os resultados:')))
i=0
negativo=0
while i<size(v):
	if v[i]<0:
		negativo=negativo+1
	i=i+1
v2=array(zeros(size(v)-negativo),dtype=float)
i=0
j=0
while i<size(v):
	if v[i]>=0:
		v2[j]=v[i]
		j=j+1
	i=i+1
print(v2)