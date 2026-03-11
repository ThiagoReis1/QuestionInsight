qf = int(input())
ql = int(input())
pcf =float(input())
pcl  = float(input())

t = 0

while(qf > ql):
	qf = qf + (qf * pcf/100)
	ql = ql + (ql * pcl/100)
	t = t + 1
print(t)