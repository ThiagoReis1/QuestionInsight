a = input("A: ")
if (a.upper() != "HISTIDINA")  and (a.upper() != "LEUCINA") and (a.upper() != "LISINA"): 
	print("Entrada:",a)
	print("Dado Invalido")
else: 
	if (a.upper() == "HISTIDINA"):
		print(round(6*12.011+10*1.0079+3*14.00674+2*15.9994,2))
	if (a.upper() == "LEUCINA"):	
		print(round(6*12.011+13*1.0079+1*14.00674+2*15.9994,2))
	if (a.upper() == "LISINA"):	
		print(round(6*12.011+15*1.0079+2*14.00674+2*15.9994,2))