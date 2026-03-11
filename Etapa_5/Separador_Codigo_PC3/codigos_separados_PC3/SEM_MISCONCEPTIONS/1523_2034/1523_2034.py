qi_baloes= int(input('digite a quantidade de baloes:'))
qc_baloes=int(input('digite a quantidade de baloes:'))
qd_baloes=int(input('digite a quantidade de baloes:'))

qf=qi_baloes
s=0
while(qf<200):
	q=(qc_baloes -qd_baloes)
	qf= qf+ q
	s=s+1
print(s)