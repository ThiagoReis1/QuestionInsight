QC=float(input("Quantidade de combo "))
VQC=QC*50

if QC<=4:
	
	print(VQC)
	

else:
	
	VD=(VQC-VQC*(12/100))
	print(round(VD,2))
	
