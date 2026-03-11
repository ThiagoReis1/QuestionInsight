from numpy import*
produtos = input("p:")
A = 16.75
L = 4.60
P = 2.85
tc=0
qa=0
ql=0
qp=0
for produto in produtos:
	if produto == 'A':
		tc += A
		qa += 1
	elif produto == 'L':
		tc += L
		ql += 1
	elif produto == 'P':
		tc += P
		qp += 1
print(round(tc,2),qa,ql,qp)
