qp = int(input("Qp: "))
qv = int(input("Qv: "))
pp = float(input("Pp: "))
pv = float(input("Pv: "))
Max = 80000
ano = 0
while ((qp + qv) <= 80000):
	qp = qp + qp*(pp/100)
	qv = qv + qv*(pv/100)
	ano = ano + 1
print(ano)