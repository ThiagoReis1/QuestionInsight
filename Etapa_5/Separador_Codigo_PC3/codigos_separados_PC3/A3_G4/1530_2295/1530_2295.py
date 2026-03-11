qp=int(input())
qv=int(input())
pp=float(input())/100
pv=float(input())/100
t = 0
while(qp + qv < 80000):
	qp = qp + (qp * pp)
	qv = qv + (qv * pv)
	qt = qp + qv 
	t = t + 1
print(t)