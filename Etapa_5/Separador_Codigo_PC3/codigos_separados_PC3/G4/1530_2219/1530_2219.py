from math import*
qp = int(input())
qv = int(input())
pg = float(input())
pv = float(input())
soma = 0
i=0

while soma<=80000:
	qp = qp +((qp/100)*pg)
	qv = qv +((qv/100)*pv)
	soma = qp + qv
	i +=1
	
print(i)
	