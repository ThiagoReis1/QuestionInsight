qp = int(input(" "))
qv = int(input(" "))
pp = float(input(" "))
pv = float(input(" "))
a = 1
qqp = 0*a*pp
qqv = 0*a*pv
qt = 0
while (qt<=80000):
	qt = qp+ (qp*qqp/100) + qv+ (qv*qqv/100)
	a = a +1
print(a)