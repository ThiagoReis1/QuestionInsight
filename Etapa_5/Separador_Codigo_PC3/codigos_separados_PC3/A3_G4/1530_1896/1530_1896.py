QP=int(input("Quantidade de pergaminhos: "))
QV=int(input("Quantidade de VARINHAS"))
PP=float(input("PERCENTUAL PERGAMINHOS:"))
PV=float(input("PERCENTUAL DE VARINHAS:"))
cont=0
A=0
A1=0
A2=0
F1=1
F2=1
while(80000>A):
	QP=QP*(PP/100)
	A1=A1+QP
	print("",A1)
	QV=QV*(PV/100)
	A1=A1+QV
	print("",A2)
	A=A+(A1+A2)
	cont=cont+1
print("",cont)