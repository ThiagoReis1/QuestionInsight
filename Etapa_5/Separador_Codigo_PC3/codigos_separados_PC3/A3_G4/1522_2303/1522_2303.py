qi = int(input())
dm = int(input())
qm = int(input())
qr = int(input())
i = qi
m = dm
M = qm
R = qr
t = 0
x = 0
while (i > R):
	saldo = i + M - R - m
	t = t + 1
	x = x + 1
print(t)