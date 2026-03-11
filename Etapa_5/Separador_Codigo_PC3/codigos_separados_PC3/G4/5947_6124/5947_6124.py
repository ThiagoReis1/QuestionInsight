CE = input("'C' se for coxinha e 'E' se for esfirra: ")
qce = int(input("A quantidade de coxinhas e esfirras: "))
qs = int(input("A quantidade de sucos: "))

if CE == 'C':
	vc = qce * 2
	vs = qs * 6
	vt = vc + vs
	print(vt)
else:
	ve = qce * 4.50
	vs = qs * 6
	vt = ve + vs
	print(vt)
	