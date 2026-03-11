from math import*

a=input("Digite o nome do aminoacido:").upper()
gli=(2*12.011+5*1.0079+14.00674+2*15.9994)
pro=(5*12.011+10*1.0079+14.00674+2*15.9994)
ser=(3*12.011+7*1.0079+14.00674+3*15.9994)
if (a=="GLICINA"):
	
	print(round(gli,2))
elif(a=="PROLINA"):
		
		print(round(pro,2))
elif(a=="SERINA"):
	
	print(round(ser,2))
else:
	
		print("Entrada:",a)
		print("Dado Invalido")