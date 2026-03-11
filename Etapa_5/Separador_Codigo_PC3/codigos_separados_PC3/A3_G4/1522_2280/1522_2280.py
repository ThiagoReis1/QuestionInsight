qi = int(input())
dm = int(input())
qm = int(input())
qr = int(input())
i = qi
m = dm
M = qm
R = qr
t = 0
while(i<R):
	i = i + M
	m = m - R
	saldo = i - m 
	moedas = saldo
	t = t + 1
print(t)