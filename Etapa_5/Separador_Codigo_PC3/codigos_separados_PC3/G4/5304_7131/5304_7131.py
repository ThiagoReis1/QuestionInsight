nidb=float(input("digite o numero inicial de bacs:  "))
qht=float(input("digite a quantidade de horas total de um experimento:  "))
while qht>=1:
	qntb=int(nidb*0.15)
	print(int(qntb+nidb))
	qht=qht-1
	nidb=nidb+qntb
	
