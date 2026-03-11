qf = int(input("Qnt de forsti: "))
ql = int(input("Qnt de loki: "))
pf = float(input("per. de forseti: "))/100
pl = float(input("per. de loki: "))/100
t = 0

while(ql<qf):
	qf = qf + qf*pf
	ql = ql + ql*pl
	t  = t +1
print(t)