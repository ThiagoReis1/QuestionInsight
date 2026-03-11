QI=float(input(":"))
QC=float(input(":"))
PI=float(input(":"))/100
PC=float(input(":"))/100
dia=0
while (QI+QC<=50000):
	QI=QI*(1+PI)
	QC=QC*(1+PC)
	dia=dia+1
print(dia)