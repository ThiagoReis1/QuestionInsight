qp = int(input())
qv = int(input())
pp = float(input())
pv = float(input())
ano = 0
while qp +qv < 80000:
	saldop = qp*(pp/100)
	qp = qp + saldop
	saldov = qv *(pv/100)
	qv = qv + saldov
	ano = ano + 1
print(ano)