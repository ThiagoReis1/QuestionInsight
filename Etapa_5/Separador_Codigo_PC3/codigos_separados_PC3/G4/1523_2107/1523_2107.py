q0=int(input("quantidade inicial: "))
qc=int(input("quantidade c: "))
qd=int(input("quantidade d: "))

m=0

while(q0<200):
	q0=q0-qd+qc
	m=m+1
print(m)

