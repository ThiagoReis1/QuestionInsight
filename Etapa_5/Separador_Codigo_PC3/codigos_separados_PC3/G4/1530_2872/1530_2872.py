qip = int (input("Informe a quantidade inicial de pergaminhos: "))
qiv = int (input("Informe a quantidade inicial de varinhas: "))
pp = float (input("Informe o percentual dos pergaminhos: "))
pv = float (input("Informe o percentual das varinhas: "))
p1 = pp/100
p2 = pv/100
i = 0
total = 0
qp = qip
qv = qiv
while (80000>=total):
	qp = qp + (qp*p1)
	qv = qv + (qv*p2)
	total = qp + qv
	i = i+1
print(i)