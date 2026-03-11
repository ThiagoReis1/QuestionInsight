qf = int(input("Seguidores Forseti:"))
ql = int(input("Seguidores Loki:"))
pf = float(input("Cresc Forseti:"))
pl = float(input("Cresc Loki:"))
t = 0
while (qf>ql) and (pl>pf):
	qf = qf + qf*pf/100
	ql = ql + ql*pl/100
	t = t+1
print(t)