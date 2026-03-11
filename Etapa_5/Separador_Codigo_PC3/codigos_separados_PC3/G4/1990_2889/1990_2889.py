
a = input ("Aminoácido: ").upper()

if (a == "GLUTAMINA"):
#C5 #H8 #N1 #O4
	PMG = (5*12.011)+(8*1.00794)+(1*14.0067)+(4*15.9994)
	print (round(PMG,2))
elif (a == "SERINA"):
#C3 #H7 #N #O3
	PMS = (3*12.011)+(7*1.00794)+(14.0067)+(3*15.9994)
	print (round (PMS,2))
elif (a == "TREONINA"):
#C4 #H9 #N #O3	
	PMT = (4*12.011)+(9*1.00794)+(14.0067)+(3*15.9994)
	print (round (PMT,2))
else: 
	print ("Entrada:" , a)
	print ("Dado Invalido")