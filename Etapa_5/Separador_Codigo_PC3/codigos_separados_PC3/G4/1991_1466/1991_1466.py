a=input()
if(a.upper()=="GLICINA"):
	b=2*12.011+5*1.0079+14.00674+2*15.9994
elif(a.upper()=="PROLINA"):
	b=5*12.011+10*1.0079+14.00674+2*15.9994
elif(a.upper()=="SERINA"):
	b=3*12.011+7*1.0079+14.00674+3*15.9994
else:
	print("Entrada: ", a)
	print("Dado Invalido")
	exit(0)
print(round(b,2))