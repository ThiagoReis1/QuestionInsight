qp = int (input("pergaminhos"))
qvm = int (input("varinhas magicas"))
pp = float (input ("percentual pergaminho"))
pv = float (input("percentual de varinhas"))

total = 0
cont = 0

fim = 80000
while (total <= fim):
	
	cont=cont +1
	qp = qp + (qp* (pp/100))
	qvm = qvm + (qvm * (pv/100))
	total=  qp + qvm
	

print (cont)


