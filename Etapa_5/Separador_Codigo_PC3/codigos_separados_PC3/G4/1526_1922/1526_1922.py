qo = int(input())
qm = int(input())
qr = int(input())

qa = qo
t = 0

while(qa > 0):
	qa = qa + qr - qm
	t = t + 1
print(t)